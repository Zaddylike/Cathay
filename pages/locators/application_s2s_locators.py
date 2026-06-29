from playwright.sync_api import Page


class ApplicationS2sLocators:
    def __init__(self, page: Page):
        self.page = page

    @property
    def btn_project_info_permission(self):
        # 專案資訊頁面_身分認證按鈕
        return self.page.locator(".sidebar__list", has=self.page.get_by_text(" 身份認證 ", exact=True))

    @property
    def page_permission(self):
        # 身分驗證頁面_logo
        return self.page.locator(".text-type--content-title")

    @property
    def tab_permission(self):
        # 身分驗證頁面_分頁_權限設定
        return self.page.locator('[role="tablist"] p-tab', has_text=" 權限設定 ")