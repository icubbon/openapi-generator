# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_call, ValidationError
from typing import Dict, List, Optional, Tuple

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictStr

from typing import Dict

from petstore_api.models.order import Order

from petstore_api.api_client import ApiClient
from petstore_api.api_response import ApiResponse
from petstore_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class StoreApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    async def delete_order(
        self,
        order_id: Annotated[StrictStr, Field(description="ID of the order that needs to be deleted")],
        **kwargs,
    ) -> None:
        """Delete purchase order by ID  # noqa: E501

        For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors  # noqa: E501

        :param order_id: ID of the order that needs to be deleted (required)
        :type order_id: str
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_order_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.delete_order_with_http_info.raw_function(
            order_id,
            **kwargs,
        )

    @validate_call
    async def delete_order_with_http_info(
        self,
        order_id: Annotated[StrictStr, Field(description="ID of the order that needs to be deleted")],
        **kwargs,
    ) -> ApiResponse:
        """Delete purchase order by ID  # noqa: E501

        For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors  # noqa: E501

        :param order_id: ID of the order that needs to be deleted (required)
        :type order_id: str
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'order_id'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_order" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['order_id'] is not None:
            _path_params['order_id'] = _params['order_id']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {}

        return await self.api_client.call_api(
            '/store/order/{order_id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    async def get_inventory(
        self,
        **kwargs,
    ) -> Dict[str, int]:
        """Returns pet inventories by status  # noqa: E501

        Returns a map of status codes to quantities  # noqa: E501

        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Dict[str, int]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_inventory_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.get_inventory_with_http_info.raw_function(
            **kwargs,
        )

    @validate_call
    async def get_inventory_with_http_info(
        self,
        **kwargs,
    ) -> ApiResponse:
        """Returns pet inventories by status  # noqa: E501

        Returns a map of status codes to quantities  # noqa: E501

        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Dict[str, int], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inventory" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = ['api_key']  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, int]",
        }

        return await self.api_client.call_api(
            '/store/inventory', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    async def get_order_by_id(
        self,
        order_id: Annotated[int, Field(le=5, strict=True, ge=1, description="ID of pet that needs to be fetched")],
        **kwargs,
    ) -> Order:
        """Find purchase order by ID  # noqa: E501

        For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions  # noqa: E501

        :param order_id: ID of pet that needs to be fetched (required)
        :type order_id: int
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Order
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_order_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.get_order_by_id_with_http_info.raw_function(
            order_id,
            **kwargs,
        )

    @validate_call
    async def get_order_by_id_with_http_info(
        self,
        order_id: Annotated[int, Field(le=5, strict=True, ge=1, description="ID of pet that needs to be fetched")],
        **kwargs,
    ) -> ApiResponse:
        """Find purchase order by ID  # noqa: E501

        For valid response try integer IDs with value <= 5 or > 10. Other values will generated exceptions  # noqa: E501

        :param order_id: ID of pet that needs to be fetched (required)
        :type order_id: int
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Order, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'order_id'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}
        if _params['order_id'] is not None:
            _path_params['order_id'] = _params['order_id']


        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Order",
            '400': None,
            '404': None,
        }

        return await self.api_client.call_api(
            '/store/order/{order_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_call
    async def place_order(
        self,
        order: Annotated[Order, Field(description="order placed for purchasing the pet")],
        **kwargs,
    ) -> Order:
        """Place an order for a pet  # noqa: E501

          # noqa: E501

        :param order: order placed for purchasing the pet (required)
        :type order: Order
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Order
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the place_order_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)

        return await self.place_order_with_http_info.raw_function(
            order,
            **kwargs,
        )

    @validate_call
    async def place_order_with_http_info(
        self,
        order: Annotated[Order, Field(description="order placed for purchasing the pet")],
        **kwargs,
    ) -> ApiResponse:
        """Place an order for a pet  # noqa: E501

          # noqa: E501

        :param order: order placed for purchasing the pet (required)
        :type order: Order
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Order, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'order'
        ]
        _all_params.extend(
            [
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method place_order" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats: Dict[str, str] = {}

        # process the path parameters
        _path_params: Dict[str, str] = {}

        # process the query parameters
        _query_params: List[Tuple[str, str]] = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        # process the body parameter
        _body_params = None
        if _params['order'] is not None:
            _body_params = _params['order']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings: List[str] = []  # noqa: E501

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Order",
            '400': None,
        }

        return await self.api_client.call_api(
            '/store/order', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
