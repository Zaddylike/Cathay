from app.omni_app import OmniApp
from config.settings import (
    BASE_URL_DEV,
    PERMISSION_S2S_APPLICATION_NAME,
    PERMISSION_SSO_APPLICATION_NAME,
)


def test_application_project_cleanup_probe(logged_app: OmniApp):
    project_abbreviation = "project-abbr-e47e"
    response_events = []

    def record_response(response):
        if response.request.method != "GET" or response.status >= 400:
            response_events.append(
                (response.request.method, response.status, response.url)
            )

    logged_app.page.on("response", record_response)

    logged_app.page.goto(BASE_URL_DEV)
    project_exists = logged_app.project_page.project_exists(project_abbreviation)

    print(f"CLEANUP_PROBE project={project_abbreviation} exists={project_exists}")

    if not project_exists:
        return

    logged_app.operate_page.go_to_permission_page(project_abbreviation)
    print(
        "CLEANUP_PROBE "
        f"baseline_sso={logged_app.single_sign_on_page.application_exists(PERMISSION_SSO_APPLICATION_NAME)}"
    )
    print(
        "CLEANUP_PROBE "
        f"test_sso={logged_app.single_sign_on_page.application_exists('sso-application-e47e')}"
    )
    print(
        "CLEANUP_PROBE "
        f"baseline_s2s={logged_app.server_to_server_page.application_exists(PERMISSION_S2S_APPLICATION_NAME)}"
    )
    print(
        "CLEANUP_PROBE "
        f"test_s2s={logged_app.server_to_server_page.application_exists('s2s-application-e47e')}"
    )

    logged_app.page.goto(BASE_URL_DEV)
    try:
        logged_app.project_page.delete_project_if_exists(project_abbreviation)
    except Exception as error:
        print(f"CLEANUP_PROBE delete_error={error}")

    logged_app.page.wait_for_timeout(2_000)
    print(f"CLEANUP_PROBE responses={response_events}")
    print(f"CLEANUP_PROBE page_text={logged_app.page.locator('body').inner_text()[-1000:]}")
