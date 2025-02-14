# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .attributes.client import AsyncAttributesClient, AttributesClient
from .auth.client import AsyncAuthClient, AuthClient
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.oauth_token_provider import OAuthTokenProvider
from .entity.client import AsyncEntityClient, EntityClient
from .environment import SayariEnvironment
from .info.client import AsyncInfoClient, InfoClient
from .notifications.client import AsyncNotificationsClient, NotificationsClient
from .project.client import AsyncProjectClient, ProjectClient
from .record.client import AsyncRecordClient, RecordClient
from .resolution.client import AsyncResolutionClient, ResolutionClient
from .resource.client import AsyncResourceClient, ResourceClient
from .search.client import AsyncSearchClient, SearchClient
from .source.client import AsyncSourceClient, SourceClient
from .supply_chain.client import AsyncSupplyChainClient, SupplyChainClient
from .trade.client import AsyncTradeClient, TradeClient
from .traversal.client import AsyncTraversalClient, TraversalClient


class BaseClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SayariEnvironment. The environment to use for requests from the client. from .environment import SayariEnvironment

                                          Defaults to SayariEnvironment.PRODUCTION

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - follow_redirects: typing.Optional[bool]. Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

        - client_id: str.

        - client_secret: str.
    ---
    from sayari.client import Sayari

    client = Sayari(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariEnvironment = SayariEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        client_id: str,
        client_secret: str
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        oauth_token_provider = OAuthTokenProvider(
            client_id=client_id,
            client_secret=client_secret,
            client_wrapper=SyncClientWrapper(
                base_url=_get_base_url(base_url=base_url, environment=environment),
                httpx_client=httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
                if follow_redirects is not None
                else httpx.Client(timeout=_defaulted_timeout),
                timeout=_defaulted_timeout,
            ),
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=oauth_token_provider.get_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.attributes = AttributesClient(client_wrapper=self._client_wrapper)
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.entity = EntityClient(client_wrapper=self._client_wrapper)
        self.info = InfoClient(client_wrapper=self._client_wrapper)
        self.notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        self.project = ProjectClient(client_wrapper=self._client_wrapper)
        self.record = RecordClient(client_wrapper=self._client_wrapper)
        self.resolution = ResolutionClient(client_wrapper=self._client_wrapper)
        self.resource = ResourceClient(client_wrapper=self._client_wrapper)
        self.search = SearchClient(client_wrapper=self._client_wrapper)
        self.source = SourceClient(client_wrapper=self._client_wrapper)
        self.supply_chain = SupplyChainClient(client_wrapper=self._client_wrapper)
        self.trade = TradeClient(client_wrapper=self._client_wrapper)
        self.traversal = TraversalClient(client_wrapper=self._client_wrapper)


class AsyncBaseClient:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SayariEnvironment. The environment to use for requests from the client. from .environment import SayariEnvironment

                                          Defaults to SayariEnvironment.PRODUCTION

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - follow_redirects: typing.Optional[bool]. Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

        - client_id: str.

        - client_secret: str.
    ---
    from sayari.client import AsyncSayari

    client = AsyncSayari(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariEnvironment = SayariEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        client_id: str,
        client_secret: str
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        oauth_token_provider = OAuthTokenProvider(
            client_id=client_id,
            client_secret=client_secret,
            client_wrapper=SyncClientWrapper(
                base_url=_get_base_url(base_url=base_url, environment=environment),
                httpx_client=httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
                if follow_redirects is not None
                else httpx.Client(timeout=_defaulted_timeout),
                timeout=_defaulted_timeout,
            ),
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=oauth_token_provider.get_token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.attributes = AsyncAttributesClient(client_wrapper=self._client_wrapper)
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.entity = AsyncEntityClient(client_wrapper=self._client_wrapper)
        self.info = AsyncInfoClient(client_wrapper=self._client_wrapper)
        self.notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        self.project = AsyncProjectClient(client_wrapper=self._client_wrapper)
        self.record = AsyncRecordClient(client_wrapper=self._client_wrapper)
        self.resolution = AsyncResolutionClient(client_wrapper=self._client_wrapper)
        self.resource = AsyncResourceClient(client_wrapper=self._client_wrapper)
        self.search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        self.source = AsyncSourceClient(client_wrapper=self._client_wrapper)
        self.supply_chain = AsyncSupplyChainClient(client_wrapper=self._client_wrapper)
        self.trade = AsyncTradeClient(client_wrapper=self._client_wrapper)
        self.traversal = AsyncTraversalClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: SayariEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
