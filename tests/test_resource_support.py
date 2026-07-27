from data.factories.resource_data import (
    build_assign_permission_test_data,
    build_permission_scenario_data,
    build_project_member_test_data,
    build_role_test_data,
)
from utils.resource_cleanup import CleanupRegistry


def test_permission_scenario_links_each_role_to_its_scope():
    data = build_permission_scenario_data("primary", "replacement")

    assert data.role_code.endswith("primary")
    assert data.scope_code.endswith("primary")
    assert data.updated_role_code.endswith("replacement")
    assert data.updated_scope_code.endswith("replacement")


def test_assign_permission_data_reuses_scenario_identifiers():
    data = build_assign_permission_test_data()

    assert data.description.removeprefix("assign-description-") in data.role_code
    assert data.second_description.removeprefix("assign-description-") in (data.updated_role_code)


def test_composed_factories_keep_existing_feature_shapes():
    member_data = build_project_member_test_data()
    role_data = build_role_test_data()

    assert member_data.project_abbreviation
    assert member_data.primary_member
    assert role_data.scope_code
    assert role_data.copied_code == f"copy-{role_data.code}"


def test_cleanup_registry_runs_once_in_reverse_order():
    calls = []
    registry = CleanupRegistry(enabled=True)

    registry.register("Scope", "scope-1", lambda: calls.append("scope"))
    registry.register("Role", "role-1", lambda: calls.append("role"))
    registry.register("Role", "role-1", lambda: calls.append("duplicate"))
    registry.cleanup()

    assert calls == ["role", "scope"]


def test_cleanup_registry_skips_cleanup_when_disabled():
    calls = []
    registry = CleanupRegistry(enabled=False)
    registry.register("Project", "project-1", lambda: calls.append("project"))

    registry.cleanup()

    assert calls == []
