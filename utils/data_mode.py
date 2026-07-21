import os
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path


ISOLATED = "isolated"
KEEP = "keep"
DATA_MODES = (ISOLATED, KEEP)


"""
用途:判斷 fixture teardown 是否需要清除測試資料。

isolated 回傳 True;keep 回傳 False。
Delete 測試本身的刪除步驟不受此函式影響。
"""
def should_cleanup(data_mode: str) -> bool:
    return data_mode == ISOLATED


"""
用途:避免多個 pytest process 同時建立 project-abbr-main baseline。

執行流程:
    1. 在 .pytest_cache 建立所有 process 共用的 lock file。
    2. 嘗試取得作業系統檔案鎖;拿不到的 process 每 0.25 秒重試。
    3. 取得鎖的 process 執行 with 區塊內的 baseline 檢查/建立。
    4. 離開 with 時，即使發生錯誤，也會在 finally 釋放檔案鎖。
    5. Windows 使用 msvcrt;macOS/Linux 使用 fcntl。

使用方式:
    with permission_project_lock():
        ensure_permission_baseline(app, create_missing=True)

注意:
    鎖只保護共用 baseline，不會鎖住後續 UUID Scope/Role 測試。
"""
@contextmanager
def permission_project_lock(timeout_seconds: int = 900) -> Iterator[None]:
    lock_path = Path(".pytest_cache") / "permission-project-main.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock_file = lock_path.open("a+b")

    lock_file.seek(0, os.SEEK_END)
    if lock_file.tell() == 0:
        lock_file.write(b"0")
        lock_file.flush()

    deadline = time.monotonic() + timeout_seconds
    acquired = False

    while not acquired:
        try:
            lock_file.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(lock_file.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl

                fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            acquired = True
        except OSError:
            if time.monotonic() >= deadline:
                lock_file.close()
                raise TimeoutError(
                    "Timed out waiting for the shared permission project lock"
                )
            time.sleep(0.25)

    try:
        yield
    finally:
        lock_file.seek(0)
        if os.name == "nt":
            import msvcrt

            msvcrt.locking(lock_file.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl

            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
        lock_file.close()
