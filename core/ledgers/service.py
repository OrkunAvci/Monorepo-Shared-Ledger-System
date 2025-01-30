from .repository import LedgerRepository
from .models import LedgerModel
import datetime

class LedgerService:
    def __init__(self, ledger_repo: LedgerRepository):
        self.ledger_repo = ledger_repo

    async def process_entry(self, owner_id: str, app: str, operation: str, amount: int, nonce: str):
        """ Validates and processes a ledger transaction """

        # Prevent duplicate transactions
        if await self.ledger_repo.nonce_exists(nonce):
            raise ValueError("Duplicate transaction detected")

        # Validate balance for negative transactions
        if amount < 0:
            balance = await self.ledger_repo.get_balance(owner_id)
            if balance + amount < 0:
                raise ValueError("Insufficient balance")

        # Create ledger entry
        entry = LedgerModel(
            owner_id=owner_id,
            app=app,
            operation=operation,
            amount=amount,
            nonce=nonce,
            created_on=datetime.datetime.now()
        )

        return await self.ledger_repo.add_entry(entry)
