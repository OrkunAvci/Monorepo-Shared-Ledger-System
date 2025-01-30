from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_session
from .schemas import LedgerEntryCreate
from .repository import LedgerRepository
from .service import LedgerService

router = APIRouter()

@router.get("/ledger/{owner_id}")
async def get_ledger_balance(owner_id: str, session: AsyncSession = Depends(get_session)):
    """ Returns the current balance for an owner """
    ledger_repo = LedgerRepository(session)
    balance = await ledger_repo.get_balance(owner_id)
    return {"owner_id": owner_id, "balance": balance}

@router.post("/ledger")
async def create_ledger_entry(entry: LedgerEntryCreate, session: AsyncSession = Depends(get_session)):
    """ Creates a new ledger entry, validating balance and duplicate transactions """
    ledger_repo = LedgerRepository(session)
    ledger_service = LedgerService(ledger_repo)

    try:
        new_entry = await ledger_service.process_entry(
            owner_id=entry.owner_id,
            app=entry.app,
            operation=entry.operation,
            amount=entry.amount,
            nonce=entry.nonce
        )
        return {"message": "Ledger entry created", "entry": new_entry}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
