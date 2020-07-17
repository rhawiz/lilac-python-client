# coding: utf-8

"""
    FDM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TradeFlowsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_flows_flow_data_flow_type_get(self, flow_type, **kwargs):  # noqa: E501
        """v1_flows_flow_data_flow_type_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_data_flow_type_get(flow_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flow_type: (required)
        :param str fields:
        :param int max_rows:
        :param str filter:
        :param str order_by:
        :return: FDMAPIDTOV1FlowsFlowData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_flows_flow_data_flow_type_get_with_http_info(flow_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_flows_flow_data_flow_type_get_with_http_info(flow_type, **kwargs)  # noqa: E501
            return data

    def v1_flows_flow_data_flow_type_get_with_http_info(self, flow_type, **kwargs):  # noqa: E501
        """v1_flows_flow_data_flow_type_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_data_flow_type_get_with_http_info(flow_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flow_type: (required)
        :param str fields:
        :param int max_rows:
        :param str filter:
        :param str order_by:
        :return: FDMAPIDTOV1FlowsFlowData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_type', 'fields', 'max_rows', 'filter', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_flows_flow_data_flow_type_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_type' is set
        if ('flow_type' not in params or
                params['flow_type'] is None):
            raise ValueError("Missing the required parameter `flow_type` when calling `v1_flows_flow_data_flow_type_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flow_type' in params:
            path_params['FlowType'] = params['flow_type']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('Fields', params['fields']))  # noqa: E501
        if 'max_rows' in params:
            query_params.append(('MaxRows', params['max_rows']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('Filter', params['filter']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('OrderBy', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey-v1']  # noqa: E501

        return self.api_client.call_api(
            '/v1/Flows/FlowData/{FlowType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FDMAPIDTOV1FlowsFlowData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_flows_flow_field_flow_type_get(self, flow_type, **kwargs):  # noqa: E501
        """v1_flows_flow_field_flow_type_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_field_flow_type_get(flow_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flow_type: (required)
        :return: list[FDMAPIDTOV1FlowsFlowField]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_flows_flow_field_flow_type_get_with_http_info(flow_type, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_flows_flow_field_flow_type_get_with_http_info(flow_type, **kwargs)  # noqa: E501
            return data

    def v1_flows_flow_field_flow_type_get_with_http_info(self, flow_type, **kwargs):  # noqa: E501
        """v1_flows_flow_field_flow_type_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_field_flow_type_get_with_http_info(flow_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flow_type: (required)
        :return: list[FDMAPIDTOV1FlowsFlowField]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_flows_flow_field_flow_type_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_type' is set
        if ('flow_type' not in params or
                params['flow_type'] is None):
            raise ValueError("Missing the required parameter `flow_type` when calling `v1_flows_flow_field_flow_type_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flow_type' in params:
            path_params['FlowType'] = params['flow_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey-v1']  # noqa: E501

        return self.api_client.call_api(
            '/v1/Flows/FlowField/{FlowType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FDMAPIDTOV1FlowsFlowField]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_flows_flow_field_value_flow_type_field_name_get(self, flow_type, field_name, **kwargs):  # noqa: E501
        """v1_flows_flow_field_value_flow_type_field_name_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_field_value_flow_type_field_name_get(flow_type, field_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flow_type: (required)
        :param str field_name: (required)
        :param str filter:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_flows_flow_field_value_flow_type_field_name_get_with_http_info(flow_type, field_name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_flows_flow_field_value_flow_type_field_name_get_with_http_info(flow_type, field_name, **kwargs)  # noqa: E501
            return data

    def v1_flows_flow_field_value_flow_type_field_name_get_with_http_info(self, flow_type, field_name, **kwargs):  # noqa: E501
        """v1_flows_flow_field_value_flow_type_field_name_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_field_value_flow_type_field_name_get_with_http_info(flow_type, field_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str flow_type: (required)
        :param str field_name: (required)
        :param str filter:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flow_type', 'field_name', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_flows_flow_field_value_flow_type_field_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flow_type' is set
        if ('flow_type' not in params or
                params['flow_type'] is None):
            raise ValueError("Missing the required parameter `flow_type` when calling `v1_flows_flow_field_value_flow_type_field_name_get`")  # noqa: E501
        # verify the required parameter 'field_name' is set
        if ('field_name' not in params or
                params['field_name'] is None):
            raise ValueError("Missing the required parameter `field_name` when calling `v1_flows_flow_field_value_flow_type_field_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'flow_type' in params:
            path_params['FlowType'] = params['flow_type']  # noqa: E501
        if 'field_name' in params:
            path_params['FieldName'] = params['field_name']  # noqa: E501

        query_params = []
        if 'filter' in params:
            query_params.append(('Filter', params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey-v1']  # noqa: E501

        return self.api_client.call_api(
            '/v1/Flows/FlowFieldValue/{FlowType}/{FieldName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_flows_flow_types_get(self, **kwargs):  # noqa: E501
        """v1_flows_flow_types_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_types_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_flows_flow_types_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_flows_flow_types_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_flows_flow_types_get_with_http_info(self, **kwargs):  # noqa: E501
        """v1_flows_flow_types_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_flows_flow_types_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_flows_flow_types_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apikey-v1']  # noqa: E501

        return self.api_client.call_api(
            '/v1/Flows/FlowTypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
