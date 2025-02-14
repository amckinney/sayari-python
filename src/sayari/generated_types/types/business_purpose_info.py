# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...base_types.types.paginated_response import PaginatedResponse
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .business_purpose_data import BusinessPurposeData


class BusinessPurposeInfo(PaginatedResponse):
    """
    Text and/or a code (NAICS, NACE, ISIC, etc.) that describes what a company is legally allowed to do or produce
    """

    data: typing.List[BusinessPurposeData]
    next: typing.Optional[typing.Any] = None
    offset: typing.Optional[int] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
