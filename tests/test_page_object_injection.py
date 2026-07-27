from app.omni_app import OmniApp
from pages.scope_page import ScopePage


def test_omni_app_injects_shared_page_dependencies():
    page = object()
    app = OmniApp(page)
    feature_pages = (
        app.project_page,
        app.project_member_page,
        app.scope_page,
        app.role_page,
        app.group_page,
        app.assign_permission_page,
        app.default_permission_page,
        app.application_permission_page,
        app.single_sign_on_page,
        app.server_to_server_page,
    )

    assert app.operate_page.base_page is app.base_page
    assert app.login_page.base_page is app.base_page

    for page_object in feature_pages:
        assert page_object.base_page is app.base_page
        assert page_object.operate_page is app.operate_page


def test_page_object_can_still_create_its_own_dependencies():
    page = object()
    scope_page = ScopePage(page)

    assert scope_page.base_page.page is page
    assert scope_page.operate_page.page is page
    assert scope_page.operate_page.base_page is scope_page.base_page
