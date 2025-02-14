# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .attribute_response_data import AttributeResponseData


class AttributeResponse(pydantic_v1.BaseModel):
    """
    OK
    ---
    from sayari import AttributeProperties, AttributeResponse, AttributeResponseData

    AttributeResponse(
        data=AttributeResponseData(
            value={
                "street1": "1600 Pennsylvania Avenue NW",
                "city": "Washington DC",
                "state": "Washington DC",
                "postalCode": "20500",
                "country": "US",
            },
            properties=[
                AttributeProperties(
                    editable=True,
                    record_count=0,
                    id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
                )
            ],
        ),
    )
    """

    data: AttributeResponseData

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
