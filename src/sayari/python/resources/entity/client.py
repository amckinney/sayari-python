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
from ..generated_types.types.country import Country
from ..generated_types.types.relationships import Relationships
from ..generated_types.types.tag import Tag
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.errors.not_found import NotFound
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.types.not_found_response import NotFoundResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from .types.entity_summary_response import EntitySummaryResponse
from .types.get_entity_response import GetEntityResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EntityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_entity(
        self,
        id: str,
        *,
        attributes_name_next: typing.Optional[str] = None,
        attributes_name_prev: typing.Optional[str] = None,
        attributes_name_limit: typing.Optional[int] = None,
        attributes_address_next: typing.Optional[str] = None,
        attributes_address_prev: typing.Optional[str] = None,
        attributes_address_limit: typing.Optional[int] = None,
        attributes_country_next: typing.Optional[str] = None,
        attributes_country_prev: typing.Optional[str] = None,
        attributes_country_limit: typing.Optional[int] = None,
        relationships_next: typing.Optional[str] = None,
        relationships_prev: typing.Optional[str] = None,
        relationships_limit: typing.Optional[int] = None,
        relationships_type: typing.Optional[Relationships] = None,
        relationships_sort: typing.Optional[str] = None,
        relationships_start_date: typing.Optional[dt.date] = None,
        relationships_end_date: typing.Optional[dt.date] = None,
        relationships_min_shares: typing.Optional[int] = None,
        relationships_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        relationships_arrival_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        relationships_arrival_state: typing.Optional[str] = None,
        relationships_arrival_city: typing.Optional[str] = None,
        relationships_departure_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        relationships_departure_state: typing.Optional[str] = None,
        relationships_departure_city: typing.Optional[str] = None,
        relationships_partner_name: typing.Optional[str] = None,
        relationships_partner_risk: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        relationships_hs_code: typing.Optional[str] = None,
        possibly_same_as_next: typing.Optional[str] = None,
        possibly_same_as_prev: typing.Optional[str] = None,
        possibly_same_as_limit: typing.Optional[int] = None,
        referenced_by_next: typing.Optional[str] = None,
        referenced_by_prev: typing.Optional[str] = None,
        referenced_by_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEntityResponse:
        """
        Retrieve an entity from the database based on the ID

        Parameters:
            - id: str. Unique identifier of the entity

            - attributes_name_next: typing.Optional[str]. The pagination token for the next page of attribute `name`.

            - attributes_name_prev: typing.Optional[str]. The pagination token for the previous page of attribute `name`.

            - attributes_name_limit: typing.Optional[int]. Limit total values returned for attribute `name`. Defaults to 100.

            - attributes_address_next: typing.Optional[str]. The pagination token for the next page of attribute `address`.

            - attributes_address_prev: typing.Optional[str]. The pagination token for the previous page of attribute `address`.

            - attributes_address_limit: typing.Optional[int]. Limit total values returned for attribute `address`. Defaults to 100.

            - attributes_country_next: typing.Optional[str]. The pagination token for the next page of attribute `country`.

            - attributes_country_prev: typing.Optional[str]. The pagination token for the previous page of attribute `country`.

            - attributes_country_limit: typing.Optional[int]. Limit total values returned for attribute `country`. Defaults to 100.

            - relationships_next: typing.Optional[str]. The pagination token for the next page of relationship results

            - relationships_prev: typing.Optional[str]. The pagination token for the previous page of relationship results

            - relationships_limit: typing.Optional[int]. Limit total relationship values. Defaults to 50.

            - relationships_type: typing.Optional[Relationships]. Filter relationships to [relationship type](/sayari-library/ontology/relationships), e.g. director_of or has_shareholder

            - relationships_sort: typing.Optional[str]. Sorts relationships by As Of date or Shareholder percentage, e.g. date or -shares

            - relationships_start_date: typing.Optional[dt.date]. Filters relationships to after a date

            - relationships_end_date: typing.Optional[dt.date]. Filters relationships to before a date

            - relationships_min_shares: typing.Optional[int]. Filters relationships to greater than or equal to a Shareholder percentage

            - relationships_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Filters relationships to a list of [countries](/sayari-library/ontology/enumerated-types#country)

            - relationships_arrival_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Filters shipment relationships to a list of arrival [countries](/sayari-library/ontology/enumerated-types#country)

            - relationships_arrival_state: typing.Optional[str]. Filters shipment relationships to an arrival state

            - relationships_arrival_city: typing.Optional[str]. Filters shipment relationships to an arrival city

            - relationships_departure_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Filters shipment relationships to a list of departure [countries](/sayari-library/ontology/enumerated-types#country)

            - relationships_departure_state: typing.Optional[str]. Filters shipment relationships to a departure state

            - relationships_departure_city: typing.Optional[str]. Filters shipment relationships to a departure city

            - relationships_partner_name: typing.Optional[str]. Filters shipment relationships to a trade partner name

            - relationships_partner_risk: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]. Filters shipment relationships to a trade partner [risk tag](/sayari-library/ontology/enumerated-types#tag)

            - relationships_hs_code: typing.Optional[str]. Filters shipment relationships to an HS code

            - possibly_same_as_next: typing.Optional[str]. The pagination token for the next page of possibly same entities.

            - possibly_same_as_prev: typing.Optional[str]. The pagination token for the previous page of possibly same entities.

            - possibly_same_as_limit: typing.Optional[int]. Limit total possibly same as entities. Defaults to 100.

            - referenced_by_next: typing.Optional[str]. The pagination token for the next page of the entity's referencing records

            - referenced_by_prev: typing.Optional[str]. The pagination token for the previous page of the entity's referencing records

            - referenced_by_limit: typing.Optional[int]. Limit totals values returned for entity's referencing records. Defaults to 100.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari-analytics.client import SayariAnalyticsApi

        client = SayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        client.entity.get_entity(id="mGq1lpuqKssNWTjIokuPeA", )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/entity/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "attributes.name.next": attributes_name_next,
                        "attributes.name.prev": attributes_name_prev,
                        "attributes.name.limit": attributes_name_limit,
                        "attributes.address.next": attributes_address_next,
                        "attributes.address.prev": attributes_address_prev,
                        "attributes.address.limit": attributes_address_limit,
                        "attributes.country.next": attributes_country_next,
                        "attributes.country.prev": attributes_country_prev,
                        "attributes.country.limit": attributes_country_limit,
                        "relationships.next": relationships_next,
                        "relationships.prev": relationships_prev,
                        "relationships.limit": relationships_limit,
                        "relationships.type": relationships_type,
                        "relationships.sort": relationships_sort,
                        "relationships.startDate": str(relationships_start_date)
                        if relationships_start_date is not None
                        else None,
                        "relationships.endDate": str(relationships_end_date)
                        if relationships_end_date is not None
                        else None,
                        "relationships.minShares": relationships_min_shares,
                        "relationships.country": relationships_country,
                        "relationships.arrivalCountry": relationships_arrival_country,
                        "relationships.arrivalState": relationships_arrival_state,
                        "relationships.arrivalCity": relationships_arrival_city,
                        "relationships.departureCountry": relationships_departure_country,
                        "relationships.departureState": relationships_departure_state,
                        "relationships.departureCity": relationships_departure_city,
                        "relationships.partnerName": relationships_partner_name,
                        "relationships.partnerRisk": relationships_partner_risk,
                        "relationships.hsCode": relationships_hs_code,
                        "possibly_same_as.next": possibly_same_as_next,
                        "possibly_same_as.prev": possibly_same_as_prev,
                        "possibly_same_as.limit": possibly_same_as_limit,
                        "referenced_by.next": referenced_by_next,
                        "referenced_by.prev": referenced_by_prev,
                        "referenced_by.limit": referenced_by_limit,
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
            return pydantic.parse_obj_as(GetEntityResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
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

    def entity_summary(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySummaryResponse:
        """
        The Entity Summary endpoint returns a smaller entity payload

        Parameters:
            - id: str. Unique identifier of the entity

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari-analytics.client import SayariAnalyticsApi

        client = SayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        client.entity.entity_summary(id="mGq1lpuqKssNWTjIokuPeA", )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/entity_summary/{jsonable_encoder(id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic.parse_obj_as(EntitySummaryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
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


class AsyncEntityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_entity(
        self,
        id: str,
        *,
        attributes_name_next: typing.Optional[str] = None,
        attributes_name_prev: typing.Optional[str] = None,
        attributes_name_limit: typing.Optional[int] = None,
        attributes_address_next: typing.Optional[str] = None,
        attributes_address_prev: typing.Optional[str] = None,
        attributes_address_limit: typing.Optional[int] = None,
        attributes_country_next: typing.Optional[str] = None,
        attributes_country_prev: typing.Optional[str] = None,
        attributes_country_limit: typing.Optional[int] = None,
        relationships_next: typing.Optional[str] = None,
        relationships_prev: typing.Optional[str] = None,
        relationships_limit: typing.Optional[int] = None,
        relationships_type: typing.Optional[Relationships] = None,
        relationships_sort: typing.Optional[str] = None,
        relationships_start_date: typing.Optional[dt.date] = None,
        relationships_end_date: typing.Optional[dt.date] = None,
        relationships_min_shares: typing.Optional[int] = None,
        relationships_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        relationships_arrival_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        relationships_arrival_state: typing.Optional[str] = None,
        relationships_arrival_city: typing.Optional[str] = None,
        relationships_departure_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        relationships_departure_state: typing.Optional[str] = None,
        relationships_departure_city: typing.Optional[str] = None,
        relationships_partner_name: typing.Optional[str] = None,
        relationships_partner_risk: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]] = None,
        relationships_hs_code: typing.Optional[str] = None,
        possibly_same_as_next: typing.Optional[str] = None,
        possibly_same_as_prev: typing.Optional[str] = None,
        possibly_same_as_limit: typing.Optional[int] = None,
        referenced_by_next: typing.Optional[str] = None,
        referenced_by_prev: typing.Optional[str] = None,
        referenced_by_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEntityResponse:
        """
        Retrieve an entity from the database based on the ID

        Parameters:
            - id: str. Unique identifier of the entity

            - attributes_name_next: typing.Optional[str]. The pagination token for the next page of attribute `name`.

            - attributes_name_prev: typing.Optional[str]. The pagination token for the previous page of attribute `name`.

            - attributes_name_limit: typing.Optional[int]. Limit total values returned for attribute `name`. Defaults to 100.

            - attributes_address_next: typing.Optional[str]. The pagination token for the next page of attribute `address`.

            - attributes_address_prev: typing.Optional[str]. The pagination token for the previous page of attribute `address`.

            - attributes_address_limit: typing.Optional[int]. Limit total values returned for attribute `address`. Defaults to 100.

            - attributes_country_next: typing.Optional[str]. The pagination token for the next page of attribute `country`.

            - attributes_country_prev: typing.Optional[str]. The pagination token for the previous page of attribute `country`.

            - attributes_country_limit: typing.Optional[int]. Limit total values returned for attribute `country`. Defaults to 100.

            - relationships_next: typing.Optional[str]. The pagination token for the next page of relationship results

            - relationships_prev: typing.Optional[str]. The pagination token for the previous page of relationship results

            - relationships_limit: typing.Optional[int]. Limit total relationship values. Defaults to 50.

            - relationships_type: typing.Optional[Relationships]. Filter relationships to [relationship type](/sayari-library/ontology/relationships), e.g. director_of or has_shareholder

            - relationships_sort: typing.Optional[str]. Sorts relationships by As Of date or Shareholder percentage, e.g. date or -shares

            - relationships_start_date: typing.Optional[dt.date]. Filters relationships to after a date

            - relationships_end_date: typing.Optional[dt.date]. Filters relationships to before a date

            - relationships_min_shares: typing.Optional[int]. Filters relationships to greater than or equal to a Shareholder percentage

            - relationships_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Filters relationships to a list of [countries](/sayari-library/ontology/enumerated-types#country)

            - relationships_arrival_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Filters shipment relationships to a list of arrival [countries](/sayari-library/ontology/enumerated-types#country)

            - relationships_arrival_state: typing.Optional[str]. Filters shipment relationships to an arrival state

            - relationships_arrival_city: typing.Optional[str]. Filters shipment relationships to an arrival city

            - relationships_departure_country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]]. Filters shipment relationships to a list of departure [countries](/sayari-library/ontology/enumerated-types#country)

            - relationships_departure_state: typing.Optional[str]. Filters shipment relationships to a departure state

            - relationships_departure_city: typing.Optional[str]. Filters shipment relationships to a departure city

            - relationships_partner_name: typing.Optional[str]. Filters shipment relationships to a trade partner name

            - relationships_partner_risk: typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]. Filters shipment relationships to a trade partner [risk tag](/sayari-library/ontology/enumerated-types#tag)

            - relationships_hs_code: typing.Optional[str]. Filters shipment relationships to an HS code

            - possibly_same_as_next: typing.Optional[str]. The pagination token for the next page of possibly same entities.

            - possibly_same_as_prev: typing.Optional[str]. The pagination token for the previous page of possibly same entities.

            - possibly_same_as_limit: typing.Optional[int]. Limit total possibly same as entities. Defaults to 100.

            - referenced_by_next: typing.Optional[str]. The pagination token for the next page of the entity's referencing records

            - referenced_by_prev: typing.Optional[str]. The pagination token for the previous page of the entity's referencing records

            - referenced_by_limit: typing.Optional[int]. Limit totals values returned for entity's referencing records. Defaults to 100.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari-analytics.client import AsyncSayariAnalyticsApi

        client = AsyncSayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        await client.entity.get_entity(id="mGq1lpuqKssNWTjIokuPeA", )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/entity/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "attributes.name.next": attributes_name_next,
                        "attributes.name.prev": attributes_name_prev,
                        "attributes.name.limit": attributes_name_limit,
                        "attributes.address.next": attributes_address_next,
                        "attributes.address.prev": attributes_address_prev,
                        "attributes.address.limit": attributes_address_limit,
                        "attributes.country.next": attributes_country_next,
                        "attributes.country.prev": attributes_country_prev,
                        "attributes.country.limit": attributes_country_limit,
                        "relationships.next": relationships_next,
                        "relationships.prev": relationships_prev,
                        "relationships.limit": relationships_limit,
                        "relationships.type": relationships_type,
                        "relationships.sort": relationships_sort,
                        "relationships.startDate": str(relationships_start_date)
                        if relationships_start_date is not None
                        else None,
                        "relationships.endDate": str(relationships_end_date)
                        if relationships_end_date is not None
                        else None,
                        "relationships.minShares": relationships_min_shares,
                        "relationships.country": relationships_country,
                        "relationships.arrivalCountry": relationships_arrival_country,
                        "relationships.arrivalState": relationships_arrival_state,
                        "relationships.arrivalCity": relationships_arrival_city,
                        "relationships.departureCountry": relationships_departure_country,
                        "relationships.departureState": relationships_departure_state,
                        "relationships.departureCity": relationships_departure_city,
                        "relationships.partnerName": relationships_partner_name,
                        "relationships.partnerRisk": relationships_partner_risk,
                        "relationships.hsCode": relationships_hs_code,
                        "possibly_same_as.next": possibly_same_as_next,
                        "possibly_same_as.prev": possibly_same_as_prev,
                        "possibly_same_as.limit": possibly_same_as_limit,
                        "referenced_by.next": referenced_by_next,
                        "referenced_by.prev": referenced_by_prev,
                        "referenced_by.limit": referenced_by_limit,
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
            return pydantic.parse_obj_as(GetEntityResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
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

    async def entity_summary(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySummaryResponse:
        """
        The Entity Summary endpoint returns a smaller entity payload

        Parameters:
            - id: str. Unique identifier of the entity

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari-analytics.client import AsyncSayariAnalyticsApi

        client = AsyncSayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        await client.entity.entity_summary(id="mGq1lpuqKssNWTjIokuPeA", )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/entity_summary/{jsonable_encoder(id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic.parse_obj_as(EntitySummaryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
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
