# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NotificationType(str, enum.Enum):
    RISK = "risk"

    def visit(self, risk: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotificationType.RISK:
            return risk()
