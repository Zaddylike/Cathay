from collections.abc import Callable

from app.omni_app import OmniApp
from data.factories.resource_data import PermissionScenarioData


def create_permission_prerequisites(
    app: OmniApp,
    data: PermissionScenarioData,
    register_cleanup: Callable[[str, str], None],
) -> None:
    scopes = (
        (data.scope_code, data.scope_name, data.scope_description),
        (
            data.updated_scope_code,
            data.updated_scope_name,
            data.updated_scope_description,
        ),
    )
    for scope_code, scope_name, scope_description in scopes:
        register_cleanup("scope", scope_code)
        app.scope_page.create_scope(scope_code, scope_name, scope_description)

    roles = (
        (data.role_code, data.role_name, data.role_description, data.scope_code),
        (
            data.updated_role_code,
            data.updated_role_name,
            data.updated_role_description,
            data.updated_scope_code,
        ),
    )
    for role_code, role_name, role_description, scope_code in roles:
        register_cleanup("role", role_code)
        app.role_page.create_role(
            role_code,
            role_name,
            role_description,
            scope_code,
        )
