from pydantic import BaseModel
from enum import Enum

class BaseLedgerOperation(Enum):
    CREDIT = "CREDIT"        # Add credits
    DEBIT = "DEBIT"          # Subtract credits
    TRANSFER = "TRANSFER"    # Move credits between accounts

# Pydantic model to validate the request body for creating a ledger entry
class LedgerEntryCreate(BaseModel):
    owner_id: str  # The ID of the user or entity
    app: str       # The app where the ledger entry belongs to
    operation: str # The ledger operation type
    amount: int    # The amount being added or subtracted
    nonce: str     # A unique identifier for the transaction (to prevent duplication)

    class Config:
        orm_mode = True  # Allows compatibility with ORM models (SQLAlchemy)