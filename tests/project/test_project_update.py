from app.omni_app import OmniApp


def test_project_update_success(logged_app: OmniApp):
    logged_app.project_page.project_update_002()
    logged_app.project_page.project_update_003()
    logged_app.project_page.project_update_004()
    logged_app.project_page.project_update_005()
    logged_app.project_page.project_update_006()
    logged_app.project_page.project_update_007()
    logged_app.project_page.project_update_008()
    logged_app.project_page.project_update_009_011()