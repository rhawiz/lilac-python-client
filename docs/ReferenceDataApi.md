# swagger_client.ReferenceDataApi

All URIs are relative to *https://sprod1.lilacfdm.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_period_types_get**](ReferenceDataApi.md#v1_period_types_get) | **GET** /v1/PeriodTypes | 
[**v1_timezones_get**](ReferenceDataApi.md#v1_timezones_get) | **GET** /v1/Timezones | 

# **v1_period_types_get**
> list[str] v1_period_types_get()



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
api_instance = swagger_client.ReferenceDataApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.v1_period_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->v1_period_types_get: %s\n" % e)
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

# **v1_timezones_get**
> list[str] v1_timezones_get()



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
api_instance = swagger_client.ReferenceDataApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.v1_timezones_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceDataApi->v1_timezones_get: %s\n" % e)
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

