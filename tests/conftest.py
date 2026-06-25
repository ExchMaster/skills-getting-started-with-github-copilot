from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASELINE_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory activities for each test to avoid state leakage."""
    # Arrange
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))

    yield

    # Cleanup
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    # Arrange
    test_client = TestClient(app)

    # Act
    yield test_client

    # Assert
    # No explicit assertions in fixture teardown.
