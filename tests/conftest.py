import pytest
from fastapi.testclient import TestClient

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)