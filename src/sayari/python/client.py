# This file was auto-generated by Fern from our API Definition.

import typing

import httpx
import time

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SayariAnalyticsApiEnvironment
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.entity.client import AsyncEntityClient, EntityClient
from .resources.record.client import AsyncRecordClient, RecordClient
from .resources.resolution.client import AsyncResolutionClient, ResolutionClient
from .resources.search.client import AsyncSearchClient, SearchClient
from .resources.source.client import AsyncSourceClient, SourceClient
from .resources.traversal.client import AsyncTraversalClient, TraversalClient


retry_limit = 3

class Retry(httpx.HTTPTransport):
    def handle_request(
        self,
        request: httpx.Request,
    ) -> httpx.Response:
        retry = 0
        resp = None
        while retry < retry_limit:
            retry += 1
            try:
                if resp is not None:
                    resp.close()
                resp = super().handle_request(request)
            # Retry on request exception
            except Exception as e:
                print("httpx {} exception {} caught - retrying".format(request.url, e))
                time.sleep(1)
                continue
            # Retry on 429
            if resp.status_code == 429:
                retry_delay = resp.headers.get("Retry-After")
                print("httpx {} 429 response - retrying after {}s".format(request.url, retry_delay))
                # Sleep for the requested amount of time
                time.sleep(int(retry_delay))
                continue
            content_type = resp.headers.get("Content-Type")
            if content_type is not None:
                mime_type, _, _ = content_type.partition(";")
                if mime_type == 'application/json':
                    try:
                        resp.read()
                        resp.json()
                    except Exception as e:
                        print("httpx {} response not valid json '{}' - retrying".format(request.url, e))
                        continue
            break
        return resp


class SayariAnalyticsApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariAnalyticsApiEnvironment = SayariAnalyticsApiEnvironment.PRODUCTION,
        client: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            client=client,
            token=token,
            httpx_client=httpx.Client(timeout=timeout, transport=Retry()),
        )
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.entity = EntityClient(client_wrapper=self._client_wrapper)
        self.record = RecordClient(client_wrapper=self._client_wrapper)
        self.resolution = ResolutionClient(client_wrapper=self._client_wrapper)
        self.search = SearchClient(client_wrapper=self._client_wrapper)
        self.source = SourceClient(client_wrapper=self._client_wrapper)
        self.traversal = TraversalClient(client_wrapper=self._client_wrapper)


class AsyncSayariAnalyticsApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariAnalyticsApiEnvironment = SayariAnalyticsApiEnvironment.PRODUCTION,
        client: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            client=client,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout, transport=Retry()),
        )
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.entity = AsyncEntityClient(client_wrapper=self._client_wrapper)
        self.record = AsyncRecordClient(client_wrapper=self._client_wrapper)
        self.resolution = AsyncResolutionClient(client_wrapper=self._client_wrapper)
        self.search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        self.source = AsyncSourceClient(client_wrapper=self._client_wrapper)
        self.traversal = AsyncTraversalClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: SayariAnalyticsApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
