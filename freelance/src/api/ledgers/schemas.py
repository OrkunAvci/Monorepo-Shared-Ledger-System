from enum import Enum

from core.ledgers.schemas import BaseLedgerOperation

class FreelancingLedgerOperation(BaseLedgerOperation, Enum):
    # BaseLedgerOperation ops are accessible by dot(.) operator.
    PROJECT_PAYMENT = "PROJECT_PAYMENT"  # Incoming payment for a project
    PROJECT_SPENDING = "PROJECT_SPENDING"  # Outgoing spending for a project
