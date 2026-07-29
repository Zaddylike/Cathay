import allure
import pytest

from app.omni_app import OmniApp


pytestmark = pytest.mark.verify_field


@allure.title("[VERIFY-FIELD] Validate Project input fields")
def test_project_field_validation(
    logged_app: OmniApp,
    project_data,
    project_cleanup,
):
    project_cleanup(project_data.project_abbreviation)

    logged_app.project_page.open_create_project_dialog()
    logged_app.project_page.validate_and_fill_project_abbreviation(
        project_data.project_abbreviation
    )
    logged_app.project_page.validate_and_fill_project_zh_name(project_data.zh_name)
    logged_app.project_page.fill_project_en_name(project_data.en_name)
    logged_app.project_page.validate_and_add_project_tags()
    logged_app.project_page.enable_project_status()
    logged_app.project_page.validate_and_fill_project_description(
        project_data.description
    )
    logged_app.project_page.select_project_icon()
    logged_app.project_page.submit_project_and_verify_created(
        project_data.project_abbreviation
    )

    logged_app.project_page.open_project_edit_form(
        project_data.project_abbreviation
    )
    logged_app.project_page.validate_and_update_project_zh_name(
        project_data.updated_zh_name
    )
    logged_app.project_page.update_project_en_name(project_data.updated_en_name)
    logged_app.project_page.update_project_tag()
    logged_app.project_page.disable_project_status()
    logged_app.project_page.update_project_description(
        project_data.updated_description
    )
    logged_app.project_page.update_project_icon()
    logged_app.project_page.submit_project_update_and_verify(
        project_data.project_abbreviation
    )
