# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.kms_v1.services.key_management_service import pagers
from google.cloud.kms_v1.types import resources
from google.cloud.kms_v1.types import service
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore
from .transports.base import KeyManagementServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import KeyManagementServiceGrpcAsyncIOTransport
from .client import KeyManagementServiceClient


class KeyManagementServiceAsyncClient:
    """Google Cloud Key Management Service

    Manages cryptographic keys and operations using those keys.
    Implements a REST model with the following objects:

    -  [KeyRing][google.cloud.kms.v1.KeyRing]
    -  [CryptoKey][google.cloud.kms.v1.CryptoKey]
    -  [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
    -  [ImportJob][google.cloud.kms.v1.ImportJob]

    If you are using manual gRPC libraries, see `Using gRPC with Cloud
    KMS <https://cloud.google.com/kms/docs/grpc>`__.
    """

    _client: KeyManagementServiceClient

    DEFAULT_ENDPOINT = KeyManagementServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = KeyManagementServiceClient.DEFAULT_MTLS_ENDPOINT

    crypto_key_path = staticmethod(KeyManagementServiceClient.crypto_key_path)
    parse_crypto_key_path = staticmethod(
        KeyManagementServiceClient.parse_crypto_key_path
    )
    crypto_key_version_path = staticmethod(
        KeyManagementServiceClient.crypto_key_version_path
    )
    parse_crypto_key_version_path = staticmethod(
        KeyManagementServiceClient.parse_crypto_key_version_path
    )
    import_job_path = staticmethod(KeyManagementServiceClient.import_job_path)
    parse_import_job_path = staticmethod(
        KeyManagementServiceClient.parse_import_job_path
    )
    key_ring_path = staticmethod(KeyManagementServiceClient.key_ring_path)
    parse_key_ring_path = staticmethod(KeyManagementServiceClient.parse_key_ring_path)
    public_key_path = staticmethod(KeyManagementServiceClient.public_key_path)
    parse_public_key_path = staticmethod(
        KeyManagementServiceClient.parse_public_key_path
    )
    common_billing_account_path = staticmethod(
        KeyManagementServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        KeyManagementServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(KeyManagementServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        KeyManagementServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        KeyManagementServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        KeyManagementServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(KeyManagementServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        KeyManagementServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(KeyManagementServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        KeyManagementServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.


        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            KeyManagementServiceAsyncClient: The constructed client.
        """
        return KeyManagementServiceClient.from_service_account_info.__func__(KeyManagementServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.


        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            KeyManagementServiceAsyncClient: The constructed client.
        """
        return KeyManagementServiceClient.from_service_account_file.__func__(KeyManagementServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.


        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return KeyManagementServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> KeyManagementServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            KeyManagementServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(KeyManagementServiceClient).get_transport_class,
        type(KeyManagementServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, KeyManagementServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the key management service client.


        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.KeyManagementServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = KeyManagementServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_key_rings(
        self,
        request: Union[service.ListKeyRingsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListKeyRingsAsyncPager:
        r"""Lists [KeyRings][google.cloud.kms.v1.KeyRing].

        .. code-block::

            from google.cloud import kms_v1

            def sample_list_key_rings():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.ListKeyRingsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_key_rings(request=request)

                # Handle the response
                for response in page_result:
                    print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.ListKeyRingsRequest, dict]):
                The request object. Request message for
                [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].
            parent (:class:`str`):
                Required. The resource name of the location associated
                with the [KeyRings][google.cloud.kms.v1.KeyRing], in the
                format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.services.key_management_service.pagers.ListKeyRingsAsyncPager:
                Response message for
                   [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListKeyRingsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_key_rings,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListKeyRingsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_crypto_keys(
        self,
        request: Union[service.ListCryptoKeysRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCryptoKeysAsyncPager:
        r"""Lists [CryptoKeys][google.cloud.kms.v1.CryptoKey].

        .. code-block::

            from google.cloud import kms_v1

            def sample_list_crypto_keys():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.ListCryptoKeysRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_crypto_keys(request=request)

                # Handle the response
                for response in page_result:
                    print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.ListCryptoKeysRequest, dict]):
                The request object. Request message for
                [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].
            parent (:class:`str`):
                Required. The resource name of the
                [KeyRing][google.cloud.kms.v1.KeyRing] to list, in the
                format ``projects/*/locations/*/keyRings/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.services.key_management_service.pagers.ListCryptoKeysAsyncPager:
                Response message for
                   [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListCryptoKeysRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_crypto_keys,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCryptoKeysAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_crypto_key_versions(
        self,
        request: Union[service.ListCryptoKeyVersionsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListCryptoKeyVersionsAsyncPager:
        r"""Lists [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion].

        .. code-block::

            from google.cloud import kms_v1

            def sample_list_crypto_key_versions():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.ListCryptoKeyVersionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_crypto_key_versions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.ListCryptoKeyVersionsRequest, dict]):
                The request object. Request message for
                [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].
            parent (:class:`str`):
                Required. The resource name of the
                [CryptoKey][google.cloud.kms.v1.CryptoKey] to list, in
                the format
                ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.services.key_management_service.pagers.ListCryptoKeyVersionsAsyncPager:
                Response message for
                   [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListCryptoKeyVersionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_crypto_key_versions,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListCryptoKeyVersionsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_import_jobs(
        self,
        request: Union[service.ListImportJobsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListImportJobsAsyncPager:
        r"""Lists [ImportJobs][google.cloud.kms.v1.ImportJob].

        .. code-block::

            from google.cloud import kms_v1

            def sample_list_import_jobs():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.ListImportJobsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_import_jobs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.ListImportJobsRequest, dict]):
                The request object. Request message for
                [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].
            parent (:class:`str`):
                Required. The resource name of the
                [KeyRing][google.cloud.kms.v1.KeyRing] to list, in the
                format ``projects/*/locations/*/keyRings/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.services.key_management_service.pagers.ListImportJobsAsyncPager:
                Response message for
                   [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.ListImportJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_import_jobs,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListImportJobsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_key_ring(
        self,
        request: Union[service.GetKeyRingRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.KeyRing:
        r"""Returns metadata for a given
        [KeyRing][google.cloud.kms.v1.KeyRing].


        .. code-block::

            from google.cloud import kms_v1

            def sample_get_key_ring():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.GetKeyRingRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_key_ring(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.GetKeyRingRequest, dict]):
                The request object. Request message for
                [KeyManagementService.GetKeyRing][google.cloud.kms.v1.KeyManagementService.GetKeyRing].
            name (:class:`str`):
                Required. The [name][google.cloud.kms.v1.KeyRing.name]
                of the [KeyRing][google.cloud.kms.v1.KeyRing] to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.KeyRing:
                A [KeyRing][google.cloud.kms.v1.KeyRing] is a toplevel logical grouping of
                   [CryptoKeys][google.cloud.kms.v1.CryptoKey].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetKeyRingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_key_ring,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_crypto_key(
        self,
        request: Union[service.GetCryptoKeyRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKey:
        r"""Returns metadata for a given
        [CryptoKey][google.cloud.kms.v1.CryptoKey], as well as its
        [primary][google.cloud.kms.v1.CryptoKey.primary]
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].


        .. code-block::

            from google.cloud import kms_v1

            def sample_get_crypto_key():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.GetCryptoKeyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_crypto_key(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.GetCryptoKeyRequest, dict]):
                The request object. Request message for
                [KeyManagementService.GetCryptoKey][google.cloud.kms.v1.KeyManagementService.GetCryptoKey].
            name (:class:`str`):
                Required. The [name][google.cloud.kms.v1.CryptoKey.name]
                of the [CryptoKey][google.cloud.kms.v1.CryptoKey] to
                get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKey:
                A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents a logical key that
                   can be used for cryptographic operations.

                   A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made
                   up of zero or more
                   [versions][google.cloud.kms.v1.CryptoKeyVersion],
                   which represent the actual key material used in
                   cryptographic operations.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetCryptoKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_crypto_key,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_crypto_key_version(
        self,
        request: Union[service.GetCryptoKeyVersionRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKeyVersion:
        r"""Returns metadata for a given
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].


        .. code-block::

            from google.cloud import kms_v1

            def sample_get_crypto_key_version():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.GetCryptoKeyVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_crypto_key_version(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.GetCryptoKeyVersionRequest, dict]):
                The request object. Request message for
                [KeyManagementService.GetCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.GetCryptoKeyVersion].
            name (:class:`str`):
                Required. The
                [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKeyVersion:
                A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an
                   individual cryptographic key, and the associated key
                   material.

                   An
                   [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                   version can be used for cryptographic operations.

                   For security reasons, the raw cryptographic key
                   material represented by a
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   can never be viewed or exported. It can only be used
                   to encrypt, decrypt, or sign data when an authorized
                   user or application invokes Cloud KMS.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetCryptoKeyVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_crypto_key_version,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_public_key(
        self,
        request: Union[service.GetPublicKeyRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.PublicKey:
        r"""Returns the public key for the given
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must
        be
        [ASYMMETRIC_SIGN][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_SIGN]
        or
        [ASYMMETRIC_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_DECRYPT].


        .. code-block::

            from google.cloud import kms_v1

            def sample_get_public_key():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.GetPublicKeyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_public_key(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.GetPublicKeyRequest, dict]):
                The request object. Request message for
                [KeyManagementService.GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].
            name (:class:`str`):
                Required. The
                [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                public key to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.PublicKey:
                The public key for a given
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].
                   Obtained via
                   [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetPublicKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_public_key,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_import_job(
        self,
        request: Union[service.GetImportJobRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.ImportJob:
        r"""Returns metadata for a given
        [ImportJob][google.cloud.kms.v1.ImportJob].


        .. code-block::

            from google.cloud import kms_v1

            def sample_get_import_job():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.GetImportJobRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_import_job(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.GetImportJobRequest, dict]):
                The request object. Request message for
                [KeyManagementService.GetImportJob][google.cloud.kms.v1.KeyManagementService.GetImportJob].
            name (:class:`str`):
                Required. The [name][google.cloud.kms.v1.ImportJob.name]
                of the [ImportJob][google.cloud.kms.v1.ImportJob] to
                get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.ImportJob:
                An [ImportJob][google.cloud.kms.v1.ImportJob] can be used to create
                   [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
                   [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                   using pre-existing key material, generated outside of
                   Cloud KMS.

                   When an [ImportJob][google.cloud.kms.v1.ImportJob] is
                   created, Cloud KMS will generate a "wrapping key",
                   which is a public/private key pair. You use the
                   wrapping key to encrypt (also known as wrap) the
                   pre-existing key material to protect it during the
                   import process. The nature of the wrapping key
                   depends on the choice of
                   [import_method][google.cloud.kms.v1.ImportJob.import_method].
                   When the wrapping key generation is complete, the
                   [state][google.cloud.kms.v1.ImportJob.state] will be
                   set to
                   [ACTIVE][google.cloud.kms.v1.ImportJob.ImportJobState.ACTIVE]
                   and the
                   [public_key][google.cloud.kms.v1.ImportJob.public_key]
                   can be fetched. The fetched public key can then be
                   used to wrap your pre-existing key material.

                   Once the key material is wrapped, it can be imported
                   into a new
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   in an existing
                   [CryptoKey][google.cloud.kms.v1.CryptoKey] by calling
                   [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].
                   Multiple
                   [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                   can be imported with a single
                   [ImportJob][google.cloud.kms.v1.ImportJob]. Cloud KMS
                   uses the private key portion of the wrapping key to
                   unwrap the key material. Only Cloud KMS has access to
                   the private key.

                   An [ImportJob][google.cloud.kms.v1.ImportJob] expires
                   3 days after it is created. Once expired, Cloud KMS
                   will no longer be able to import or unwrap any key
                   material that was wrapped with the
                   [ImportJob][google.cloud.kms.v1.ImportJob]'s public
                   key.

                   For more information, see [Importing a
                   key](\ https://cloud.google.com/kms/docs/importing-a-key).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GetImportJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_import_job,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_key_ring(
        self,
        request: Union[service.CreateKeyRingRequest, dict] = None,
        *,
        parent: str = None,
        key_ring_id: str = None,
        key_ring: resources.KeyRing = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.KeyRing:
        r"""Create a new [KeyRing][google.cloud.kms.v1.KeyRing] in a given
        Project and Location.


        .. code-block::

            from google.cloud import kms_v1

            def sample_create_key_ring():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.CreateKeyRingRequest(
                    parent="parent_value",
                    key_ring_id="key_ring_id_value",
                )

                # Make the request
                response = client.create_key_ring(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.CreateKeyRingRequest, dict]):
                The request object. Request message for
                [KeyManagementService.CreateKeyRing][google.cloud.kms.v1.KeyManagementService.CreateKeyRing].
            parent (:class:`str`):
                Required. The resource name of the location associated
                with the [KeyRings][google.cloud.kms.v1.KeyRing], in the
                format ``projects/*/locations/*``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            key_ring_id (:class:`str`):
                Required. It must be unique within a location and match
                the regular expression ``[a-zA-Z0-9_-]{1,63}``

                This corresponds to the ``key_ring_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            key_ring (:class:`google.cloud.kms_v1.types.KeyRing`):
                Required. A [KeyRing][google.cloud.kms.v1.KeyRing] with
                initial field values.

                This corresponds to the ``key_ring`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.KeyRing:
                A [KeyRing][google.cloud.kms.v1.KeyRing] is a toplevel logical grouping of
                   [CryptoKeys][google.cloud.kms.v1.CryptoKey].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, key_ring_id, key_ring])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateKeyRingRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if key_ring_id is not None:
            request.key_ring_id = key_ring_id
        if key_ring is not None:
            request.key_ring = key_ring

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_key_ring,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_crypto_key(
        self,
        request: Union[service.CreateCryptoKeyRequest, dict] = None,
        *,
        parent: str = None,
        crypto_key_id: str = None,
        crypto_key: resources.CryptoKey = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKey:
        r"""Create a new [CryptoKey][google.cloud.kms.v1.CryptoKey] within a
        [KeyRing][google.cloud.kms.v1.KeyRing].

        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] and
        [CryptoKey.version_template.algorithm][google.cloud.kms.v1.CryptoKeyVersionTemplate.algorithm]
        are required.


        .. code-block::

            from google.cloud import kms_v1

            def sample_create_crypto_key():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.CreateCryptoKeyRequest(
                    parent="parent_value",
                    crypto_key_id="crypto_key_id_value",
                )

                # Make the request
                response = client.create_crypto_key(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.CreateCryptoKeyRequest, dict]):
                The request object. Request message for
                [KeyManagementService.CreateCryptoKey][google.cloud.kms.v1.KeyManagementService.CreateCryptoKey].
            parent (:class:`str`):
                Required. The [name][google.cloud.kms.v1.KeyRing.name]
                of the KeyRing associated with the
                [CryptoKeys][google.cloud.kms.v1.CryptoKey].

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            crypto_key_id (:class:`str`):
                Required. It must be unique within a KeyRing and match
                the regular expression ``[a-zA-Z0-9_-]{1,63}``

                This corresponds to the ``crypto_key_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            crypto_key (:class:`google.cloud.kms_v1.types.CryptoKey`):
                Required. A [CryptoKey][google.cloud.kms.v1.CryptoKey]
                with initial field values.

                This corresponds to the ``crypto_key`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKey:
                A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents a logical key that
                   can be used for cryptographic operations.

                   A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made
                   up of zero or more
                   [versions][google.cloud.kms.v1.CryptoKeyVersion],
                   which represent the actual key material used in
                   cryptographic operations.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, crypto_key_id, crypto_key])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateCryptoKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if crypto_key_id is not None:
            request.crypto_key_id = crypto_key_id
        if crypto_key is not None:
            request.crypto_key = crypto_key

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_crypto_key,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_crypto_key_version(
        self,
        request: Union[service.CreateCryptoKeyVersionRequest, dict] = None,
        *,
        parent: str = None,
        crypto_key_version: resources.CryptoKeyVersion = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKeyVersion:
        r"""Create a new
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in a
        [CryptoKey][google.cloud.kms.v1.CryptoKey].

        The server will assign the next sequential id. If unset,
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will be set
        to
        [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED].


        .. code-block::

            from google.cloud import kms_v1

            def sample_create_crypto_key_version():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.CreateCryptoKeyVersionRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_crypto_key_version(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.CreateCryptoKeyVersionRequest, dict]):
                The request object. Request message for
                [KeyManagementService.CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion].
            parent (:class:`str`):
                Required. The [name][google.cloud.kms.v1.CryptoKey.name]
                of the [CryptoKey][google.cloud.kms.v1.CryptoKey]
                associated with the
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion].

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            crypto_key_version (:class:`google.cloud.kms_v1.types.CryptoKeyVersion`):
                Required. A
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                with initial field values.

                This corresponds to the ``crypto_key_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKeyVersion:
                A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an
                   individual cryptographic key, and the associated key
                   material.

                   An
                   [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                   version can be used for cryptographic operations.

                   For security reasons, the raw cryptographic key
                   material represented by a
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   can never be viewed or exported. It can only be used
                   to encrypt, decrypt, or sign data when an authorized
                   user or application invokes Cloud KMS.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, crypto_key_version])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateCryptoKeyVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if crypto_key_version is not None:
            request.crypto_key_version = crypto_key_version

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_crypto_key_version,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def import_crypto_key_version(
        self,
        request: Union[service.ImportCryptoKeyVersionRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKeyVersion:
        r"""Import wrapped key material into a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].

        All requests must specify a
        [CryptoKey][google.cloud.kms.v1.CryptoKey]. If a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] is
        additionally specified in the request, key material will be
        reimported into that version. Otherwise, a new version will be
        created, and will be assigned the next sequential id within the
        [CryptoKey][google.cloud.kms.v1.CryptoKey].


        .. code-block::

            from google.cloud import kms_v1

            def sample_import_crypto_key_version():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.ImportCryptoKeyVersionRequest(
                    rsa_aes_wrapped_key=b'rsa_aes_wrapped_key_blob',
                    parent="parent_value",
                    algorithm="EXTERNAL_SYMMETRIC_ENCRYPTION",
                    import_job="import_job_value",
                )

                # Make the request
                response = client.import_crypto_key_version(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.ImportCryptoKeyVersionRequest, dict]):
                The request object. Request message for
                [KeyManagementService.ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKeyVersion:
                A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an
                   individual cryptographic key, and the associated key
                   material.

                   An
                   [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                   version can be used for cryptographic operations.

                   For security reasons, the raw cryptographic key
                   material represented by a
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   can never be viewed or exported. It can only be used
                   to encrypt, decrypt, or sign data when an authorized
                   user or application invokes Cloud KMS.

        """
        # Create or coerce a protobuf request object.
        request = service.ImportCryptoKeyVersionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.import_crypto_key_version,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_import_job(
        self,
        request: Union[service.CreateImportJobRequest, dict] = None,
        *,
        parent: str = None,
        import_job_id: str = None,
        import_job: resources.ImportJob = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.ImportJob:
        r"""Create a new [ImportJob][google.cloud.kms.v1.ImportJob] within a
        [KeyRing][google.cloud.kms.v1.KeyRing].

        [ImportJob.import_method][google.cloud.kms.v1.ImportJob.import_method]
        is required.


        .. code-block::

            from google.cloud import kms_v1

            def sample_create_import_job():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                import_job = kms_v1.ImportJob()
                import_job.import_method = "RSA_OAEP_4096_SHA1_AES_256"
                import_job.protection_level = "EXTERNAL_VPC"

                request = kms_v1.CreateImportJobRequest(
                    parent="parent_value",
                    import_job_id="import_job_id_value",
                    import_job=import_job,
                )

                # Make the request
                response = client.create_import_job(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.CreateImportJobRequest, dict]):
                The request object. Request message for
                [KeyManagementService.CreateImportJob][google.cloud.kms.v1.KeyManagementService.CreateImportJob].
            parent (:class:`str`):
                Required. The [name][google.cloud.kms.v1.KeyRing.name]
                of the [KeyRing][google.cloud.kms.v1.KeyRing] associated
                with the [ImportJobs][google.cloud.kms.v1.ImportJob].

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            import_job_id (:class:`str`):
                Required. It must be unique within a KeyRing and match
                the regular expression ``[a-zA-Z0-9_-]{1,63}``

                This corresponds to the ``import_job_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            import_job (:class:`google.cloud.kms_v1.types.ImportJob`):
                Required. An [ImportJob][google.cloud.kms.v1.ImportJob]
                with initial field values.

                This corresponds to the ``import_job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.ImportJob:
                An [ImportJob][google.cloud.kms.v1.ImportJob] can be used to create
                   [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
                   [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                   using pre-existing key material, generated outside of
                   Cloud KMS.

                   When an [ImportJob][google.cloud.kms.v1.ImportJob] is
                   created, Cloud KMS will generate a "wrapping key",
                   which is a public/private key pair. You use the
                   wrapping key to encrypt (also known as wrap) the
                   pre-existing key material to protect it during the
                   import process. The nature of the wrapping key
                   depends on the choice of
                   [import_method][google.cloud.kms.v1.ImportJob.import_method].
                   When the wrapping key generation is complete, the
                   [state][google.cloud.kms.v1.ImportJob.state] will be
                   set to
                   [ACTIVE][google.cloud.kms.v1.ImportJob.ImportJobState.ACTIVE]
                   and the
                   [public_key][google.cloud.kms.v1.ImportJob.public_key]
                   can be fetched. The fetched public key can then be
                   used to wrap your pre-existing key material.

                   Once the key material is wrapped, it can be imported
                   into a new
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   in an existing
                   [CryptoKey][google.cloud.kms.v1.CryptoKey] by calling
                   [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].
                   Multiple
                   [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                   can be imported with a single
                   [ImportJob][google.cloud.kms.v1.ImportJob]. Cloud KMS
                   uses the private key portion of the wrapping key to
                   unwrap the key material. Only Cloud KMS has access to
                   the private key.

                   An [ImportJob][google.cloud.kms.v1.ImportJob] expires
                   3 days after it is created. Once expired, Cloud KMS
                   will no longer be able to import or unwrap any key
                   material that was wrapped with the
                   [ImportJob][google.cloud.kms.v1.ImportJob]'s public
                   key.

                   For more information, see [Importing a
                   key](\ https://cloud.google.com/kms/docs/importing-a-key).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, import_job_id, import_job])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.CreateImportJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if import_job_id is not None:
            request.import_job_id = import_job_id
        if import_job is not None:
            request.import_job = import_job

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_import_job,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_crypto_key(
        self,
        request: Union[service.UpdateCryptoKeyRequest, dict] = None,
        *,
        crypto_key: resources.CryptoKey = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKey:
        r"""Update a [CryptoKey][google.cloud.kms.v1.CryptoKey].

        .. code-block::

            from google.cloud import kms_v1

            def sample_update_crypto_key():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.UpdateCryptoKeyRequest(
                )

                # Make the request
                response = client.update_crypto_key(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.UpdateCryptoKeyRequest, dict]):
                The request object. Request message for
                [KeyManagementService.UpdateCryptoKey][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKey].
            crypto_key (:class:`google.cloud.kms_v1.types.CryptoKey`):
                Required. [CryptoKey][google.cloud.kms.v1.CryptoKey]
                with updated values.

                This corresponds to the ``crypto_key`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. List of fields to be
                updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKey:
                A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents a logical key that
                   can be used for cryptographic operations.

                   A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made
                   up of zero or more
                   [versions][google.cloud.kms.v1.CryptoKeyVersion],
                   which represent the actual key material used in
                   cryptographic operations.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([crypto_key, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.UpdateCryptoKeyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if crypto_key is not None:
            request.crypto_key = crypto_key
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_crypto_key,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("crypto_key.name", request.crypto_key.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_crypto_key_version(
        self,
        request: Union[service.UpdateCryptoKeyVersionRequest, dict] = None,
        *,
        crypto_key_version: resources.CryptoKeyVersion = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKeyVersion:
        r"""Update a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s
        metadata.

        [state][google.cloud.kms.v1.CryptoKeyVersion.state] may be
        changed between
        [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
        and
        [DISABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DISABLED]
        using this method. See
        [DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion]
        and
        [RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion]
        to move between other states.


        .. code-block::

            from google.cloud import kms_v1

            def sample_update_crypto_key_version():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.UpdateCryptoKeyVersionRequest(
                )

                # Make the request
                response = client.update_crypto_key_version(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.UpdateCryptoKeyVersionRequest, dict]):
                The request object. Request message for
                [KeyManagementService.UpdateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyVersion].
            crypto_key_version (:class:`google.cloud.kms_v1.types.CryptoKeyVersion`):
                Required.
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                with updated values.

                This corresponds to the ``crypto_key_version`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Required. List of fields to be
                updated in this request.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKeyVersion:
                A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an
                   individual cryptographic key, and the associated key
                   material.

                   An
                   [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                   version can be used for cryptographic operations.

                   For security reasons, the raw cryptographic key
                   material represented by a
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   can never be viewed or exported. It can only be used
                   to encrypt, decrypt, or sign data when an authorized
                   user or application invokes Cloud KMS.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([crypto_key_version, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.UpdateCryptoKeyVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if crypto_key_version is not None:
            request.crypto_key_version = crypto_key_version
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_crypto_key_version,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("crypto_key_version.name", request.crypto_key_version.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_crypto_key_primary_version(
        self,
        request: Union[service.UpdateCryptoKeyPrimaryVersionRequest, dict] = None,
        *,
        name: str = None,
        crypto_key_version_id: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKey:
        r"""Update the version of a
        [CryptoKey][google.cloud.kms.v1.CryptoKey] that will be used in
        [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

        Returns an error if called on a key whose purpose is not
        [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].


        .. code-block::

            from google.cloud import kms_v1

            def sample_update_crypto_key_primary_version():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.UpdateCryptoKeyPrimaryVersionRequest(
                    name="name_value",
                    crypto_key_version_id="crypto_key_version_id_value",
                )

                # Make the request
                response = client.update_crypto_key_primary_version(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.UpdateCryptoKeyPrimaryVersionRequest, dict]):
                The request object. Request message for
                [KeyManagementService.UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKey][google.cloud.kms.v1.CryptoKey] to update.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            crypto_key_version_id (:class:`str`):
                Required. The id of the child
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to use as primary.

                This corresponds to the ``crypto_key_version_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKey:
                A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents a logical key that
                   can be used for cryptographic operations.

                   A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made
                   up of zero or more
                   [versions][google.cloud.kms.v1.CryptoKeyVersion],
                   which represent the actual key material used in
                   cryptographic operations.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, crypto_key_version_id])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.UpdateCryptoKeyPrimaryVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if crypto_key_version_id is not None:
            request.crypto_key_version_id = crypto_key_version_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_crypto_key_primary_version,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def destroy_crypto_key_version(
        self,
        request: Union[service.DestroyCryptoKeyVersionRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKeyVersion:
        r"""Schedule a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] for
        destruction.

        Upon calling this method,
        [CryptoKeyVersion.state][google.cloud.kms.v1.CryptoKeyVersion.state]
        will be set to
        [DESTROY_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY_SCHEDULED],
        and
        [destroy_time][google.cloud.kms.v1.CryptoKeyVersion.destroy_time]
        will be set to the time
        [destroy_scheduled_duration][google.cloud.kms.v1.CryptoKey.destroy_scheduled_duration]
        in the future. At that time, the
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will
        automatically change to
        [DESTROYED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROYED],
        and the key material will be irrevocably destroyed.

        Before the
        [destroy_time][google.cloud.kms.v1.CryptoKeyVersion.destroy_time]
        is reached,
        [RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion]
        may be called to reverse the process.


        .. code-block::

            from google.cloud import kms_v1

            def sample_destroy_crypto_key_version():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.DestroyCryptoKeyVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.destroy_crypto_key_version(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.DestroyCryptoKeyVersionRequest, dict]):
                The request object. Request message for
                [KeyManagementService.DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to destroy.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKeyVersion:
                A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an
                   individual cryptographic key, and the associated key
                   material.

                   An
                   [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                   version can be used for cryptographic operations.

                   For security reasons, the raw cryptographic key
                   material represented by a
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   can never be viewed or exported. It can only be used
                   to encrypt, decrypt, or sign data when an authorized
                   user or application invokes Cloud KMS.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.DestroyCryptoKeyVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.destroy_crypto_key_version,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def restore_crypto_key_version(
        self,
        request: Union[service.RestoreCryptoKeyVersionRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> resources.CryptoKeyVersion:
        r"""Restore a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in the
        [DESTROY_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY_SCHEDULED]
        state.

        Upon restoration of the CryptoKeyVersion,
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will be set
        to
        [DISABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DISABLED],
        and
        [destroy_time][google.cloud.kms.v1.CryptoKeyVersion.destroy_time]
        will be cleared.


        .. code-block::

            from google.cloud import kms_v1

            def sample_restore_crypto_key_version():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.RestoreCryptoKeyVersionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.restore_crypto_key_version(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.RestoreCryptoKeyVersionRequest, dict]):
                The request object. Request message for
                [KeyManagementService.RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to restore.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.CryptoKeyVersion:
                A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an
                   individual cryptographic key, and the associated key
                   material.

                   An
                   [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                   version can be used for cryptographic operations.

                   For security reasons, the raw cryptographic key
                   material represented by a
                   [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                   can never be viewed or exported. It can only be used
                   to encrypt, decrypt, or sign data when an authorized
                   user or application invokes Cloud KMS.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.RestoreCryptoKeyVersionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.restore_crypto_key_version,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def encrypt(
        self,
        request: Union[service.EncryptRequest, dict] = None,
        *,
        name: str = None,
        plaintext: bytes = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.EncryptResponse:
        r"""Encrypts data, so that it can only be recovered by a call to
        [Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must
        be
        [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].


        .. code-block::

            from google.cloud import kms_v1

            def sample_encrypt():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.EncryptRequest(
                    name="name_value",
                    plaintext=b'plaintext_blob',
                )

                # Make the request
                response = client.encrypt(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.EncryptRequest, dict]):
                The request object. Request message for
                [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKey][google.cloud.kms.v1.CryptoKey] or
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to use for encryption.

                If a [CryptoKey][google.cloud.kms.v1.CryptoKey] is
                specified, the server will use its [primary
                version][google.cloud.kms.v1.CryptoKey.primary].

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            plaintext (:class:`bytes`):
                Required. The data to encrypt. Must be no larger than
                64KiB.

                The maximum size depends on the key version's
                [protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level].
                For
                [SOFTWARE][google.cloud.kms.v1.ProtectionLevel.SOFTWARE]
                keys, the plaintext must be no larger than 64KiB. For
                [HSM][google.cloud.kms.v1.ProtectionLevel.HSM] keys, the
                combined length of the plaintext and
                additional_authenticated_data fields must be no larger
                than 8KiB.

                This corresponds to the ``plaintext`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.EncryptResponse:
                Response message for
                   [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, plaintext])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.EncryptRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if plaintext is not None:
            request.plaintext = plaintext

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.encrypt,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def decrypt(
        self,
        request: Union[service.DecryptRequest, dict] = None,
        *,
        name: str = None,
        ciphertext: bytes = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.DecryptResponse:
        r"""Decrypts data that was protected by
        [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must
        be
        [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].


        .. code-block::

            from google.cloud import kms_v1

            def sample_decrypt():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.DecryptRequest(
                    name="name_value",
                    ciphertext=b'ciphertext_blob',
                )

                # Make the request
                response = client.decrypt(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.DecryptRequest, dict]):
                The request object. Request message for
                [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKey][google.cloud.kms.v1.CryptoKey] to use for
                decryption. The server will choose the appropriate
                version.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ciphertext (:class:`bytes`):
                Required. The encrypted data originally returned in
                [EncryptResponse.ciphertext][google.cloud.kms.v1.EncryptResponse.ciphertext].

                This corresponds to the ``ciphertext`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.DecryptResponse:
                Response message for
                   [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, ciphertext])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.DecryptRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if ciphertext is not None:
            request.ciphertext = ciphertext

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.decrypt,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def asymmetric_sign(
        self,
        request: Union[service.AsymmetricSignRequest, dict] = None,
        *,
        name: str = None,
        digest: service.Digest = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.AsymmetricSignResponse:
        r"""Signs data using a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] with
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        ASYMMETRIC_SIGN, producing a signature that can be verified with
        the public key retrieved from
        [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].


        .. code-block::

            from google.cloud import kms_v1

            def sample_asymmetric_sign():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.AsymmetricSignRequest(
                    name="name_value",
                )

                # Make the request
                response = client.asymmetric_sign(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.AsymmetricSignRequest, dict]):
                The request object. Request message for
                [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to use for signing.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            digest (:class:`google.cloud.kms_v1.types.Digest`):
                Optional. The digest of the data to sign. The digest
                must be produced with the same digest algorithm as
                specified by the key version's
                [algorithm][google.cloud.kms.v1.CryptoKeyVersion.algorithm].

                This field may not be supplied if
                [AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data]
                is supplied.

                This corresponds to the ``digest`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.AsymmetricSignResponse:
                Response message for
                   [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, digest])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.AsymmetricSignRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if digest is not None:
            request.digest = digest

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.asymmetric_sign,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def asymmetric_decrypt(
        self,
        request: Union[service.AsymmetricDecryptRequest, dict] = None,
        *,
        name: str = None,
        ciphertext: bytes = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.AsymmetricDecryptResponse:
        r"""Decrypts data that was encrypted with a public key retrieved
        from
        [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey]
        corresponding to a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] with
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        ASYMMETRIC_DECRYPT.


        .. code-block::

            from google.cloud import kms_v1

            def sample_asymmetric_decrypt():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.AsymmetricDecryptRequest(
                    name="name_value",
                    ciphertext=b'ciphertext_blob',
                )

                # Make the request
                response = client.asymmetric_decrypt(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.AsymmetricDecryptRequest, dict]):
                The request object. Request message for
                [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to use for decryption.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ciphertext (:class:`bytes`):
                Required. The data encrypted with the named
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s
                public key using OAEP.

                This corresponds to the ``ciphertext`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.AsymmetricDecryptResponse:
                Response message for
                   [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, ciphertext])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.AsymmetricDecryptRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if ciphertext is not None:
            request.ciphertext = ciphertext

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.asymmetric_decrypt,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def mac_sign(
        self,
        request: Union[service.MacSignRequest, dict] = None,
        *,
        name: str = None,
        data: bytes = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.MacSignResponse:
        r"""Signs data using a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] with
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] MAC,
        producing a tag that can be verified by another source with the
        same key.


        .. code-block::

            from google.cloud import kms_v1

            def sample_mac_sign():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.MacSignRequest(
                    name="name_value",
                    data=b'data_blob',
                )

                # Make the request
                response = client.mac_sign(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.MacSignRequest, dict]):
                The request object. Request message for
                [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to use for signing.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            data (:class:`bytes`):
                Required. The data to sign. The MAC
                tag is computed over this data field
                based on the specific algorithm.

                This corresponds to the ``data`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.MacSignResponse:
                Response message for
                   [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, data])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.MacSignRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if data is not None:
            request.data = data

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.mac_sign,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def mac_verify(
        self,
        request: Union[service.MacVerifyRequest, dict] = None,
        *,
        name: str = None,
        data: bytes = None,
        mac: bytes = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.MacVerifyResponse:
        r"""Verifies MAC tag using a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] with
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] MAC,
        and returns a response that indicates whether or not the
        verification was successful.


        .. code-block::

            from google.cloud import kms_v1

            def sample_mac_verify():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.MacVerifyRequest(
                    name="name_value",
                    data=b'data_blob',
                    mac=b'mac_blob',
                )

                # Make the request
                response = client.mac_verify(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.MacVerifyRequest, dict]):
                The request object. Request message for
                [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].
            name (:class:`str`):
                Required. The resource name of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                to use for verification.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            data (:class:`bytes`):
                Required. The data used previously as a
                [MacSignRequest.data][google.cloud.kms.v1.MacSignRequest.data]
                to generate the MAC tag.

                This corresponds to the ``data`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            mac (:class:`bytes`):
                Required. The signature to verify.
                This corresponds to the ``mac`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.MacVerifyResponse:
                Response message for
                   [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, data, mac])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.MacVerifyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if data is not None:
            request.data = data
        if mac is not None:
            request.mac = mac

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.mac_verify,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def generate_random_bytes(
        self,
        request: Union[service.GenerateRandomBytesRequest, dict] = None,
        *,
        location: str = None,
        length_bytes: int = None,
        protection_level: resources.ProtectionLevel = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> service.GenerateRandomBytesResponse:
        r"""Generate random bytes using the Cloud KMS randomness
        source in the provided location.


        .. code-block::

            from google.cloud import kms_v1

            def sample_generate_random_bytes():
                # Create a client
                client = kms_v1.KeyManagementServiceClient()

                # Initialize request argument(s)
                request = kms_v1.GenerateRandomBytesRequest(
                )

                # Make the request
                response = client.generate_random_bytes(request=request)

                # Handle the response
                print(response)


        Args:
            request (Union[google.cloud.kms_v1.types.GenerateRandomBytesRequest, dict]):
                The request object. Request message for
                [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].
            location (:class:`str`):
                The project-specific location in
                which to generate random bytes. For
                example,
                "projects/my-project/locations/us-central1".

                This corresponds to the ``location`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            length_bytes (:class:`int`):
                The length in bytes of the amount of
                randomness to retrieve.  Minimum 8
                bytes, maximum 1024 bytes.

                This corresponds to the ``length_bytes`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            protection_level (:class:`google.cloud.kms_v1.types.ProtectionLevel`):
                The
                [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
                to use when generating the random data. Currently, only
                [HSM][google.cloud.kms.v1.ProtectionLevel.HSM]
                protection level is supported.

                This corresponds to the ``protection_level`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.kms_v1.types.GenerateRandomBytesResponse:
                Response message for
                   [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([location, length_bytes, protection_level])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = service.GenerateRandomBytesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if location is not None:
            request.location = location
        if length_bytes is not None:
            request.length_bytes = length_bytes
        if protection_level is not None:
            request.protection_level = protection_level

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.generate_random_bytes,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("location", request.location),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the IAM access control policy on the specified function.

        Replaces any existing policy.


        Args:
            request (:class:`~.policy_pb2.SetIamPolicyRequest`):
                The request object. Request message for `SetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**::

                    {
                      "bindings": [
                        {
                          "role": "roles/resourcemanager.organizationAdmin",
                          "members": [
                            "user:mike@example.com",
                            "group:admins@example.com",
                            "domain:google.com",
                            "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                          ]
                        },
                        {
                          "role": "roles/resourcemanager.organizationViewer",
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**::

                    bindings:
                    - members:
                      - user:mike@example.com
                      - group:admins@example.com
                      - domain:google.com
                      - serviceAccount:my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin
                    - members:
                      - user:eve@example.com
                      role: roles/resourcemanager.organizationViewer
                      condition:
                        title: expirable access
                        description: Does not grant access after Sep 2020
                        expression: request.time < timestamp('2020-10-01T00:00:00.000Z')

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.SetIamPolicyRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.set_iam_policy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the IAM access control policy for a function.

        Returns an empty policy if the function exists and does
        not have a policy set.


        Args:
            request (:class:`~.iam_policy_pb2.GetIamPolicyRequest`):
                The request object. Request message for `GetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**::

                    {
                      "bindings": [
                        {
                          "role": "roles/resourcemanager.organizationAdmin",
                          "members": [
                            "user:mike@example.com",
                            "group:admins@example.com",
                            "domain:google.com",
                            "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                          ]
                        },
                        {
                          "role": "roles/resourcemanager.organizationViewer",
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**::

                    bindings:
                    - members:
                      - user:mike@example.com
                      - group:admins@example.com
                      - domain:google.com
                      - serviceAccount:my-project-id@appspot.gserviceaccount.com
                      role: roles/resourcemanager.organizationAdmin
                    - members:
                      - user:eve@example.com
                      role: roles/resourcemanager.organizationViewer
                      condition:
                        title: expirable access
                        description: Does not grant access after Sep 2020
                        expression: request.time < timestamp('2020-10-01T00:00:00.000Z')

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.GetIamPolicyRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_iam_policy,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Tests the specified permissions against the IAM access control
            policy for a function.

        If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.


        Args:
            request (:class:`~.iam_policy_pb2.TestIamPermissionsRequest`):
                The request object. Request message for
                `TestIamPermissions` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~iam_policy_pb2.PolicyTestIamPermissionsResponse:
                Response message for ``TestIamPermissions`` method.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.TestIamPermissionsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.test_iam_permissions,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-kms",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("KeyManagementServiceAsyncClient",)
