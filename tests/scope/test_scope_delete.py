from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-CRUD] Delete scope successfully")
def test_scope_delete_success(logged_app: OmniApp):
    logged_app.scope_page.open_scope_delete_dialog()
    logged_app.scope_page.verify_delete_confirm_disabled_by_default()
    logged_app.scope_page.cancel_scope_delete_then_reopen()
    logged_app.scope_page.confirm_scope_delete()
    logged_app.scope_page.verify_scope_deleted()
