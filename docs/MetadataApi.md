# swagger_client.MetadataApi

All URIs are relative to *https://sprod1.lilacfdm.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_metadata_curve_id_get**](MetadataApi.md#v1_metadata_curve_id_get) | **GET** /v1/Metadata/{CurveID} | 
[**v1_metadata_register_curve_tag_post**](MetadataApi.md#v1_metadata_register_curve_tag_post) | **POST** /v1/Metadata/RegisterCurveTag | 
[**v1_metadata_register_tag_post**](MetadataApi.md#v1_metadata_register_tag_post) | **POST** /v1/Metadata/RegisterTag | 
[**v1_metadata_search_get**](MetadataApi.md#v1_metadata_search_get) | **GET** /v1/Metadata/Search | 
[**v1_metadata_tag_types_get**](MetadataApi.md#v1_metadata_tag_types_get) | **GET** /v1/Metadata/TagTypes | 

# **v1_metadata_curve_id_get**
> FDMAPIDTOV1CurveMetadata v1_metadata_curve_id_get(curve_id)



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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 

try:
    api_response = api_instance.v1_metadata_curve_id_get(curve_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->v1_metadata_curve_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 

### Return type

[**FDMAPIDTOV1CurveMetadata**](FDMAPIDTOV1CurveMetadata.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_metadata_register_curve_tag_post**
> v1_metadata_register_curve_tag_post(curve_id=curve_id, tag_name=tag_name, tag_value=tag_value)



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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int |  (optional)
tag_name = 'tag_name_example' # str |  (optional)
tag_value = 'tag_value_example' # str |  (optional)

try:
    api_instance.v1_metadata_register_curve_tag_post(curve_id=curve_id, tag_name=tag_name, tag_value=tag_value)
except ApiException as e:
    print("Exception when calling MetadataApi->v1_metadata_register_curve_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | [optional] 
 **tag_name** | **str**|  | [optional] 
 **tag_value** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_metadata_register_tag_post**
> v1_metadata_register_tag_post(tag_name=tag_name)



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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
tag_name = 'tag_name_example' # str |  (optional)

try:
    api_instance.v1_metadata_register_tag_post(tag_name=tag_name)
except ApiException as e:
    print("Exception when calling MetadataApi->v1_metadata_register_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_metadata_search_get**
> list[FDMAPIDTOV1CurveMetadata] v1_metadata_search_get(query=query, max_results=max_results, skip_rows=skip_rows)



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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str |  (optional)
max_results = 100 # int |  (optional) (default to 100)
skip_rows = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.v1_metadata_search_get(query=query, max_results=max_results, skip_rows=skip_rows)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->v1_metadata_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **max_results** | **int**|  | [optional] [default to 100]
 **skip_rows** | **int**|  | [optional] [default to 0]

### Return type

[**list[FDMAPIDTOV1CurveMetadata]**](FDMAPIDTOV1CurveMetadata.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_metadata_tag_types_get**
> list[str] v1_metadata_tag_types_get()



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
api_instance = swagger_client.MetadataApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.v1_metadata_tag_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->v1_metadata_tag_types_get: %s\n" % e)
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

