from enum import Enum

from core.ledgers.schemas import BaseLedgerOperation

class ContentLedgerOperation(BaseLedgerOperation, Enum):
    # BaseLedgerOperation ops are accessible by dot(.) operator.
    CONTENT_CREATION = "CONTENT_CREATION" # Spend credits to publish content
    CONTENT_ACCESS = "CONTENT_ACCESS"    # Adjust credits for accessing premium content
