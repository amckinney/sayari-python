# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..generated_types.types.both_identifier_types import BothIdentifierTypes
from ..generated_types.types.country import Country
from ..generated_types.types.entities import Entities
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
from .types.resolution_response import ResolutionResponse


class ResolutionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def resolution(
        self,
        *,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]] = None,
        country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        address: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contact: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters:
            - name: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity name

            - identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]]. Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.

            - country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)

            - address: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity address

            - date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity date of birth

            - contact: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity contact

            - type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]. [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.resolution.resolution(
            name="victoria beckham limited",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/resolution"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        "identifier": identifier,
                        "country": country,
                        "address": address,
                        "date_of_birth": date_of_birth,
                        "contact": contact,
                        "type": type,
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
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ResolutionResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncResolutionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def resolution(
        self,
        *,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]] = None,
        country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        address: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contact: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters:
            - name: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity name

            - identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]]. Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.

            - country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)

            - address: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity address

            - date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity date of birth

            - contact: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Entity contact

            - type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]. [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.resolution.resolution(
            name="victoria beckham limited",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/resolution"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        "identifier": identifier,
                        "country": country,
                        "address": address,
                        "date_of_birth": date_of_birth,
                        "contact": contact,
                        "type": type,
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
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ResolutionResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
