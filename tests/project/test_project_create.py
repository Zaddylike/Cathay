from app.omni_app import OmniApp


def test_project_create_success(logged_app: OmniApp):
    logged_app.project_page.project_create_002()
    logged_app.project_page.project_create_003()
    logged_app.project_page.project_create_004()
    logged_app.project_page.project_create_005()
    logged_app.project_page.project_create_006()
    logged_app.project_page.project_create_007()
    logged_app.project_page.project_create_008()
    logged_app.project_page.project_create_009()
    logged_app.project_page.project_create_010_011()