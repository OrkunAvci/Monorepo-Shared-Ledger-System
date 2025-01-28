import enum

class BaseLedgerOperation(enum.Enum):
    CREDIT = "CREDIT"        # Add credits
    DEBIT = "DEBIT"          # Subtract credits
    TRANSFER = "TRANSFER"    # Move credits between accounts