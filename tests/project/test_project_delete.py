from app.omni_app import OmniApp


def test_project_delete_success(logged_app: OmniApp):
    logged_app.project_page.project_delete_002()
    logged_app.project_page.project_delete_003()
    logged_app.project_page.project_delete_004()
    logged_app.project_page.project_delete_005()
