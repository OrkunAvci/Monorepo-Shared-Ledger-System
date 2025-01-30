from fastapi.testclient import TestClient
from core.main import app
from core.ledgers.schemas import LedgerEntryCreate
import pytest

client = TestClient(app)

# Sample test data
test_ledger_data = {
    "owner_id": "user123",
    "app": "content",
    "operation": "DAILY_REWARD",
    "amount": 10,
    "nonce": "nonce_123"
}

# Sample data for GET /ledger/{owner_id}
test_balance_data = {"owner_id": "user123"}

def test_get_ledger_balance():
    """ Test GET /ledger/{owner_id} endpoint """
    # Test a valid owner_id
    response = client.get("/ledger/user123")
    assert response.status_code == 200
    assert response.json() == {"owner_id": "user123", "balance": 0}

    # Test a non-existing owner_id
    response = client.get("/ledger/nonexistent_user")
    assert response.status_code == 200
    assert response.json() == {"owner_id": "nonexistent_user", "balance": 0}

def test_create_ledger_entry():
    """ Test POST /ledger endpoint """
    entry = LedgerEntryCreate(**test_ledger_data)
    # POST to create a ledger entry
    response = client.post("/ledger", json=entry.dict())
    
    assert response.status_code == 200
    assert response.json() == {"message": "Ledger entry created", "entry": {
        "owner_id": "user123",
        "app": "content",
        "operation": "DAILY_REWARD",
        "amount": 10,
        "nonce": "nonce_123"
    }}

def test_create_duplicate_nonce():
    """ Test POST /ledger with duplicate nonce """
    entry = LedgerEntryCreate(**test_ledger_data)
    # First POST request
    response = client.post("/ledger", json=entry.dict())
    assert response.status_code == 200
    
    # Second POST request with same nonce (should raise error)
    response = client.post("/ledger", json=entry.dict())
    assert response.status_code == 400
    assert response.json() == {"detail": "Duplicate transaction detected"}

def test_insufficient_balance():
    """ Test POST /ledger with insufficient balance for negative operations """
    # Negative operation: Try to subtract more than available balance
    test_ledger_data["operation"] = "CREDIT_SPEND"
    test_ledger_data["amount"] = -100  # Try spending 100, but initial balance is 0
    
    entry = LedgerEntryCreate(**test_ledger_data)
    
    # First POST request to check insufficient balance
    response = client.post("/ledger", json=entry.dict())
    assert response.status_code == 400
    assert response.json() == {"detail": "Insufficient balance"}
