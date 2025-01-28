from enum import Enum

from core.ledgers.schemas import BaseLedgerOperation

class FreelancingLedgerOperation(BaseLedgerOperation):
    PROJECT_PAYMENT = "PROJECT_PAYMENT"  # Credit: Incoming payment for a project
    PROJECT_SPENDING = "PROJECT_SPENDING"  # Debit: Outgoing spending for a project
