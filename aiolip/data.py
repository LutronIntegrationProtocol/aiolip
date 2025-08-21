"""LIP data structures and enums for aiolip."""

from dataclasses import dataclass
from enum import Enum


@dataclass
class LIPMessage:
    """Class for LIP messages."""

    mode: str
    integration_id: int
    action_number: int
    value: float


class LIPConenctionState(Enum):
    """Enum for LIP connection states."""

    NOT_CONNECTED = 0
    CONNECTING = 1
    CONNECTED = 2


class LIPMode(Enum):
    """Enum for LIP protocol modes."""

    OUTPUT = "OUTPUT"
    DEVICE = "DEVICE"
    UNKNOWN = -1


LIP_PROTOCOL_MODE_TO_LIPMODE = {"OUTPUT": LIPMode.OUTPUT, "DEVICE": LIPMode.DEVICE}
