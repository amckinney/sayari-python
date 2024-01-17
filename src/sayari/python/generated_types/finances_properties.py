# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .currency import Currency
from .finance_type import FinanceType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FinancesProperties(pydantic.BaseModel):
    context: typing.Optional[FinanceType] = pydantic.Field(description="The type of figure")
    currency: typing.Optional[Currency] = pydantic.Field(description="The currency, if applicable")
    date: typing.Optional[str] = pydantic.Field(description="as-of date")
    from_date: typing.Optional[str] = pydantic.Field(description="start date")
    to_date: typing.Optional[str] = pydantic.Field(description="end date")
    type: typing.Optional[str] = pydantic.Field(description="A free-text definition of the type")
    value: float = pydantic.Field(description="The numerical amount")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
