# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...generated_types.types.risk import Risk
from ...shared_types.types.risk_value import RiskValue
from .notification_additional_information import NotificationAdditionalInformation
from .notification_type import NotificationType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Notification(pydantic.BaseModel):
    type: NotificationType = pydantic.Field(description="The type of notification, currently limited to 'risk'")
    field: Risk = pydantic.Field(description="The field that the notification is for")
    values: typing.List[RiskValue] = pydantic.Field(description="The previous values of the field")
    date: str = pydantic.Field(description="The date the notification was created")
    additional_information: typing.Optional[NotificationAdditionalInformation] = None

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
