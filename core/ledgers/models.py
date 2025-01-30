from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class LedgerModel(Base):
    __tablename__ = "ledger_entries"  # Single table for all ledgers

    id = Column(Integer, primary_key=True, autoincrement=True)
    app = Column(String, nullable=False)  # Defines the app using this ledger
    operation = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, unique=True, nullable=False)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow, nullable=False)
