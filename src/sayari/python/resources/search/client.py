# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.errors.not_acceptable import NotAcceptable
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.types.not_acceptable_response import NotAcceptableResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from ..shared_types.types.search_field import SearchField
from .types.entity_search_results import EntitySearchResults
from .types.filter_list import FilterList
from .types.record_search_results import RecordSearchResults

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_entity(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: str,
        filter: typing.Optional[FilterList] = OMIT,
        fields: typing.Optional[typing.List[SearchField]] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        geo_facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
    ) -> EntitySearchResults:
        """
        Search for an entity

        Parameters:
            - limit: typing.Optional[int]. A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

            - offset: typing.Optional[int]. Number of results to skip before returning response. Defaults to 0.

            - q: str. Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

            - filter: typing.Optional[FilterList]. Filters to be applied to search query to limit the result-set.

            - fields: typing.Optional[typing.List[SearchField]]. Record or entity fields to search against.

            - facets: typing.Optional[bool]. Whether or not to return search facets in results giving counts by field. Defaults to false.

            - geo_facets: typing.Optional[bool]. Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

            - advanced: typing.Optional[bool]. Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if fields is not OMIT:
            _request["fields"] = fields
        if facets is not OMIT:
            _request["facets"] = facets
        if geo_facets is not OMIT:
            _request["geo_facets"] = geo_facets
        if advanced is not OMIT:
            _request["advanced"] = advanced
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/search/entity"),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EntitySearchResults, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    def search_record(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: str,
        filter: typing.Optional[FilterList] = OMIT,
        fields: typing.Optional[typing.List[SearchField]] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        geo_facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
    ) -> RecordSearchResults:
        """
        Search for a record

        Parameters:
            - limit: typing.Optional[int]. A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

            - offset: typing.Optional[int]. Number of results to skip before returning response. Defaults to 0.

            - q: str. Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

            - filter: typing.Optional[FilterList]. Filters to be applied to search query to limit the result-set.

            - fields: typing.Optional[typing.List[SearchField]]. Record or entity fields to search against.

            - facets: typing.Optional[bool]. Whether or not to return search facets in results giving counts by field. Defaults to false.

            - geo_facets: typing.Optional[bool]. Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

            - advanced: typing.Optional[bool]. Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if fields is not OMIT:
            _request["fields"] = fields
        if facets is not OMIT:
            _request["facets"] = facets
        if geo_facets is not OMIT:
            _request["geo_facets"] = geo_facets
        if advanced is not OMIT:
            _request["advanced"] = advanced
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/search/record"),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecordSearchResults, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_entity(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: str,
        filter: typing.Optional[FilterList] = OMIT,
        fields: typing.Optional[typing.List[SearchField]] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        geo_facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
    ) -> EntitySearchResults:
        """
        Search for an entity

        Parameters:
            - limit: typing.Optional[int]. A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

            - offset: typing.Optional[int]. Number of results to skip before returning response. Defaults to 0.

            - q: str. Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

            - filter: typing.Optional[FilterList]. Filters to be applied to search query to limit the result-set.

            - fields: typing.Optional[typing.List[SearchField]]. Record or entity fields to search against.

            - facets: typing.Optional[bool]. Whether or not to return search facets in results giving counts by field. Defaults to false.

            - geo_facets: typing.Optional[bool]. Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

            - advanced: typing.Optional[bool]. Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if fields is not OMIT:
            _request["fields"] = fields
        if facets is not OMIT:
            _request["facets"] = facets
        if geo_facets is not OMIT:
            _request["geo_facets"] = geo_facets
        if advanced is not OMIT:
            _request["advanced"] = advanced
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/search/entity"),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EntitySearchResults, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    async def search_record(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: str,
        filter: typing.Optional[FilterList] = OMIT,
        fields: typing.Optional[typing.List[SearchField]] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        geo_facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
    ) -> RecordSearchResults:
        """
        Search for a record

        Parameters:
            - limit: typing.Optional[int]. A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

            - offset: typing.Optional[int]. Number of results to skip before returning response. Defaults to 0.

            - q: str. Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

            - filter: typing.Optional[FilterList]. Filters to be applied to search query to limit the result-set.

            - fields: typing.Optional[typing.List[SearchField]]. Record or entity fields to search against.

            - facets: typing.Optional[bool]. Whether or not to return search facets in results giving counts by field. Defaults to false.

            - geo_facets: typing.Optional[bool]. Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

            - advanced: typing.Optional[bool]. Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if fields is not OMIT:
            _request["fields"] = fields
        if facets is not OMIT:
            _request["facets"] = facets
        if geo_facets is not OMIT:
            _request["geo_facets"] = geo_facets
        if advanced is not OMIT:
            _request["advanced"] = advanced
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/search/record"),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecordSearchResults, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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
