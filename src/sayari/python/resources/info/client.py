# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.not_found import NotFound
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.not_found_response import NotFoundResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from .types.history_response import HistoryResponse
from .types.usage_response import UsageResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_usage(
        self,
        *,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsageResponse:
        """
        The usage endpoint provides a simple interface to retrieve information on usage made by your API account. This includes both views per API path and credits consumed. The time period for the usage query is also specified in the response and whether or not this includes total usage.

        Parameters:
            - from_: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the starting time period to obtain usage stats. In the format YYYY-MM-DD

            - to: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the ending time period to obtain usage stats. In the format YYYY-MM-DD

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/usage"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "from": str(from_) if from_ is not None else None,
                        "to": str(to) if to is not None else None,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UsageResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_history(
        self,
        *,
        events: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        size: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HistoryResponse:
        """
        The history endpoint return a user's event history.

        Parameters:
            - events: typing.Optional[typing.Union[str, typing.Sequence[str]]]. The type of events to filter on.

            - from_: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the starting time period for the events. In the format YYYY-MM-DD

            - to: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the ending time period for the events. In the format YYYY-MM-DD

            - size: typing.Optional[int]. Size to limit number of events returned

            - token: typing.Optional[str]. Pagination token to retrieve the next page of results

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/history"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "events": events,
                        "from": str(from_) if from_ is not None else None,
                        "to": str(to) if to is not None else None,
                        "size": size,
                        "token": token,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(HistoryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_usage(
        self,
        *,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UsageResponse:
        """
        The usage endpoint provides a simple interface to retrieve information on usage made by your API account. This includes both views per API path and credits consumed. The time period for the usage query is also specified in the response and whether or not this includes total usage.

        Parameters:
            - from_: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the starting time period to obtain usage stats. In the format YYYY-MM-DD

            - to: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the ending time period to obtain usage stats. In the format YYYY-MM-DD

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/usage"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "from": str(from_) if from_ is not None else None,
                        "to": str(to) if to is not None else None,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UsageResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_history(
        self,
        *,
        events: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        size: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HistoryResponse:
        """
        The history endpoint return a user's event history.

        Parameters:
            - events: typing.Optional[typing.Union[str, typing.Sequence[str]]]. The type of events to filter on.

            - from_: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the starting time period for the events. In the format YYYY-MM-DD

            - to: typing.Optional[dt.date]. An ISO 8601 encoded date string indicating the ending time period for the events. In the format YYYY-MM-DD

            - size: typing.Optional[int]. Size to limit number of events returned

            - token: typing.Optional[str]. Pagination token to retrieve the next page of results

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/history"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "events": events,
                        "from": str(from_) if from_ is not None else None,
                        "to": str(to) if to is not None else None,
                        "size": size,
                        "token": token,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(HistoryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
