"""Exceptions for the Lutron Integration Protocol (LIP)."""


class LIPConnectionStateError(Exception):
    """An exception to represent a conneciton state error."""

    def __str__(self) -> str:
        """Return string representation."""
        return "Lutron Integration Protcol is not connected."


class LIPProtocolError(Exception):
    """An exception to represent a protocol error."""

    def __init__(self, received, expected):
        """Initialize the protocol error with received and expected values."""
        self.received = received
        self.expected = expected

    def __str__(self) -> str:
        """Return string representation."""
        return (
            f"Lutron Protocol Error received=[{self.received}] "
            f"expected=[{self.expected}]"
        )
