from app.omni_app import OmniApp
import allure


@allure.title("[SCOPE-COPY] Copy scope successfully")
def test_scope_copy_success(logged_app: OmniApp):
    logged_app.scope_page.open_scope_copy_dialog()
    logged_app.scope_page.validate_and_fill_copied_scope_code()
    logged_app.scope_page.validate_and_fill_copied_scope_name()
    logged_app.scope_page.submit_scope_copy_and_verify()
