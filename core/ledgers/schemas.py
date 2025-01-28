from enum import Enum

class BaseLedgerOperation(Enum):
    CREDIT = "CREDIT"        # Add credits
    DEBIT = "DEBIT"          # Subtract credits
    TRANSFER = "TRANSFER"    # Move credits between accounts