# swagger_client.TradeFlowsApi

All URIs are relative to *https://sprod1.lilacfdm.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_flows_flow_data_flow_type_get**](TradeFlowsApi.md#v1_flows_flow_data_flow_type_get) | **GET** /v1/Flows/FlowData/{FlowType} | 
[**v1_flows_flow_field_flow_type_get**](TradeFlowsApi.md#v1_flows_flow_field_flow_type_get) | **GET** /v1/Flows/FlowField/{FlowType} | 
[**v1_flows_flow_field_value_flow_type_field_name_get**](TradeFlowsApi.md#v1_flows_flow_field_value_flow_type_field_name_get) | **GET** /v1/Flows/FlowFieldValue/{FlowType}/{FieldName} | 
[**v1_flows_flow_types_get**](TradeFlowsApi.md#v1_flows_flow_types_get) | **GET** /v1/Flows/FlowTypes | 

# **v1_flows_flow_data_flow_type_get**
> FDMAPIDTOV1FlowsFlowData v1_flows_flow_data_flow_type_get(flow_type, fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey-v1
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TradeFlowsApi(swagger_client.ApiClient(configuration))
flow_type = 'flow_type_example' # str | 
fields = 'fields_example' # str |  (optional)
max_rows = 56 # int |  (optional)
filter = '' # str |  (optional)
order_by = '' # str |  (optional)

try:
    api_response = api_instance.v1_flows_flow_data_flow_type_get(flow_type, fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeFlowsApi->v1_flows_flow_data_flow_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_type** | **str**|  | 
 **fields** | **str**|  | [optional] 
 **max_rows** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**FDMAPIDTOV1FlowsFlowData**](FDMAPIDTOV1FlowsFlowData.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_flows_flow_field_flow_type_get**
> list[FDMAPIDTOV1FlowsFlowField] v1_flows_flow_field_flow_type_get(flow_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey-v1
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TradeFlowsApi(swagger_client.ApiClient(configuration))
flow_type = 'flow_type_example' # str | 

try:
    api_response = api_instance.v1_flows_flow_field_flow_type_get(flow_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeFlowsApi->v1_flows_flow_field_flow_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_type** | **str**|  | 

### Return type

[**list[FDMAPIDTOV1FlowsFlowField]**](FDMAPIDTOV1FlowsFlowField.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_flows_flow_field_value_flow_type_field_name_get**
> list[str] v1_flows_flow_field_value_flow_type_field_name_get(flow_type, field_name, filter=filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey-v1
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TradeFlowsApi(swagger_client.ApiClient(configuration))
flow_type = 'flow_type_example' # str | 
field_name = 'field_name_example' # str | 
filter = '' # str |  (optional)

try:
    api_response = api_instance.v1_flows_flow_field_value_flow_type_field_name_get(flow_type, field_name, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeFlowsApi->v1_flows_flow_field_value_flow_type_field_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_type** | **str**|  | 
 **field_name** | **str**|  | 
 **filter** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_flows_flow_types_get**
> list[str] v1_flows_flow_types_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apikey-v1
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TradeFlowsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.v1_flows_flow_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TradeFlowsApi->v1_flows_flow_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

