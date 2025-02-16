from fastapi.testclient import TestClient
from main import app

client = TestClient(app)  # ✅ Correct, no `base_url`
