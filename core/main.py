from fastapi import FastAPI
from core.ledgers.api_routes import router as ledger_router

# Create the FastAPI app
app = FastAPI()

# Include ledger routes (and other app routes)
app.include_router(ledger_router, prefix="/ledger", tags=["ledger"])
