from collections.abc import Callable
from dataclasses import dataclass, field

import allure


@dataclass(frozen=True)
class CleanupAction:
    key: tuple[str, str]
    name: str
    callback: Callable[[], None]


@dataclass
class CleanupRegistry:
    enabled: bool
    _actions: list[CleanupAction] = field(default_factory=list)
    _keys: set[tuple[str, str]] = field(default_factory=set)

    def register(
        self,
        resource_type: str,
        identifier: str,
        callback: Callable[[], None],
    ) -> None:
        key = (resource_type, identifier)
        if key in self._keys:
            return

        self._keys.add(key)
        self._actions.append(
            CleanupAction(
                key=key,
                name=f"{resource_type} cleanup failed: {identifier}",
                callback=callback,
            )
        )

    def cleanup(self) -> None:
        if not self.enabled:
            return

        for action in reversed(self._actions):
            try:
                action.callback()
            except Exception as error:
                allure.attach(
                    str(error),
                    name=action.name,
                    attachment_type=allure.attachment_type.TEXT,
                )
