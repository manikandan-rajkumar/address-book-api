import os
import sys

import pytest
from fastapi.testclient import TestClient

from app.main import app

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


@pytest.fixture
def client():
    return TestClient(app)
