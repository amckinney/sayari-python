# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FinanceType(str, enum.Enum):
    """
    Finance type enums describe financial information about an entity; typically used to describe the cumulative monetary value of share capital issued by a company or held by an individual shareholder
    """

    SHARE_PERCENTAGE = "share_percentage"
    """
    Percentage ownership of a given company's share capital, represented as a value from 0-100
    """

    SHARE_AMOUNT = "share_amount"
    """
    Cumulative monetary value of one or more company shares, typically either held by a shareholder or issued by the company
    """

    REGISTERED_CAPITAL = "registered_capital"
    """
    Cumulative monetary value of the share capital of a given company
    """

    PAID_UP_CAPITAL = "paid_up_capital"
    """
    Cumulative monetary value of the share capital for which one or more shareholders have paid a given company
    """

    AUTHORIZED_CAPITAL = "authorized_capital"
    """
    The maximum amount of share capital a company is allowed to issue under its legal statutes
    """

    SUBSCRIBED_CAPITAL = "subscribed_capital"
    """
    Cumulative monetary value of the share capital held by shareholders of a given company
    """

    def visit(
        self,
        share_percentage: typing.Callable[[], T_Result],
        share_amount: typing.Callable[[], T_Result],
        registered_capital: typing.Callable[[], T_Result],
        paid_up_capital: typing.Callable[[], T_Result],
        authorized_capital: typing.Callable[[], T_Result],
        subscribed_capital: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FinanceType.SHARE_PERCENTAGE:
            return share_percentage()
        if self is FinanceType.SHARE_AMOUNT:
            return share_amount()
        if self is FinanceType.REGISTERED_CAPITAL:
            return registered_capital()
        if self is FinanceType.PAID_UP_CAPITAL:
            return paid_up_capital()
        if self is FinanceType.AUTHORIZED_CAPITAL:
            return authorized_capital()
        if self is FinanceType.SUBSCRIBED_CAPITAL:
            return subscribed_capital()
