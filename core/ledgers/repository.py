from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import LedgerModel

class LedgerRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_balance(self, owner_id: str) -> int:
        """ Returns the total balance for an owner """
        result = await self.session.execute(
            select(LedgerModel.amount).where(LedgerModel.owner_id == owner_id)
        )
        return sum(row[0] for row in result.all())

    async def nonce_exists(self, nonce: str) -> bool:
        """ Checks if a nonce already exists (prevents duplicate transactions) """
        result = await self.session.execute(
            select(LedgerModel.id).where(LedgerModel.nonce == nonce)
        )
        return result.scalar() is not None

    async def add_entry(self, entry: LedgerModel):
        """ Adds a new ledger entry """
        self.session.add(entry)
        await self.session.commit()
        return entry
