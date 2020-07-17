# swagger_client.RefineryUnitsAndTurnaroundsApi

All URIs are relative to *https://sprod1.lilacfdm.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_iir_ref_turnaround_daily_data_get**](RefineryUnitsAndTurnaroundsApi.md#v1_iir_ref_turnaround_daily_data_get) | **GET** /v1/IIR/RefTurnaroundDailyData | 
[**v1_iir_ref_turnaround_data_get**](RefineryUnitsAndTurnaroundsApi.md#v1_iir_ref_turnaround_data_get) | **GET** /v1/IIR/RefTurnaroundData | 
[**v1_iir_ref_turnaround_field_get**](RefineryUnitsAndTurnaroundsApi.md#v1_iir_ref_turnaround_field_get) | **GET** /v1/IIR/RefTurnaroundField | 
[**v1_iir_ref_turnaround_field_value_field_name_get**](RefineryUnitsAndTurnaroundsApi.md#v1_iir_ref_turnaround_field_value_field_name_get) | **GET** /v1/IIR/RefTurnaroundFieldValue/{FieldName} | 
[**v1_iir_ref_unit_data_get**](RefineryUnitsAndTurnaroundsApi.md#v1_iir_ref_unit_data_get) | **GET** /v1/IIR/RefUnitData | 
[**v1_iir_ref_unit_field_get**](RefineryUnitsAndTurnaroundsApi.md#v1_iir_ref_unit_field_get) | **GET** /v1/IIR/RefUnitField | 
[**v1_iir_ref_unit_field_value_field_name_get**](RefineryUnitsAndTurnaroundsApi.md#v1_iir_ref_unit_field_value_field_name_get) | **GET** /v1/IIR/RefUnitFieldValue/{FieldName} | 

# **v1_iir_ref_turnaround_daily_data_get**
> FDMAPIDTOV1IIRIIRData v1_iir_ref_turnaround_daily_data_get(fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)



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
api_instance = swagger_client.RefineryUnitsAndTurnaroundsApi(swagger_client.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
max_rows = 56 # int |  (optional)
filter = '' # str |  (optional)
order_by = '' # str |  (optional)

try:
    api_response = api_instance.v1_iir_ref_turnaround_daily_data_get(fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineryUnitsAndTurnaroundsApi->v1_iir_ref_turnaround_daily_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **max_rows** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**FDMAPIDTOV1IIRIIRData**](FDMAPIDTOV1IIRIIRData.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_iir_ref_turnaround_data_get**
> FDMAPIDTOV1IIRIIRData v1_iir_ref_turnaround_data_get(fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)



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
api_instance = swagger_client.RefineryUnitsAndTurnaroundsApi(swagger_client.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
max_rows = 56 # int |  (optional)
filter = '' # str |  (optional)
order_by = '' # str |  (optional)

try:
    api_response = api_instance.v1_iir_ref_turnaround_data_get(fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineryUnitsAndTurnaroundsApi->v1_iir_ref_turnaround_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **max_rows** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**FDMAPIDTOV1IIRIIRData**](FDMAPIDTOV1IIRIIRData.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_iir_ref_turnaround_field_get**
> list[FDMAPIDTOV1IIRIIRField] v1_iir_ref_turnaround_field_get(is_daily_turnaround=is_daily_turnaround)



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
api_instance = swagger_client.RefineryUnitsAndTurnaroundsApi(swagger_client.ApiClient(configuration))
is_daily_turnaround = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.v1_iir_ref_turnaround_field_get(is_daily_turnaround=is_daily_turnaround)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineryUnitsAndTurnaroundsApi->v1_iir_ref_turnaround_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_daily_turnaround** | **bool**|  | [optional] [default to false]

### Return type

[**list[FDMAPIDTOV1IIRIIRField]**](FDMAPIDTOV1IIRIIRField.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_iir_ref_turnaround_field_value_field_name_get**
> list[str] v1_iir_ref_turnaround_field_value_field_name_get(field_name, filter=filter, is_daily_turnaround=is_daily_turnaround)



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
api_instance = swagger_client.RefineryUnitsAndTurnaroundsApi(swagger_client.ApiClient(configuration))
field_name = 'field_name_example' # str | 
filter = '' # str |  (optional)
is_daily_turnaround = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.v1_iir_ref_turnaround_field_value_field_name_get(field_name, filter=filter, is_daily_turnaround=is_daily_turnaround)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineryUnitsAndTurnaroundsApi->v1_iir_ref_turnaround_field_value_field_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**|  | 
 **filter** | **str**|  | [optional] 
 **is_daily_turnaround** | **bool**|  | [optional] [default to false]

### Return type

**list[str]**

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_iir_ref_unit_data_get**
> FDMAPIDTOV1IIRIIRData v1_iir_ref_unit_data_get(fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)



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
api_instance = swagger_client.RefineryUnitsAndTurnaroundsApi(swagger_client.ApiClient(configuration))
fields = 'fields_example' # str |  (optional)
max_rows = 56 # int |  (optional)
filter = '' # str |  (optional)
order_by = '' # str |  (optional)

try:
    api_response = api_instance.v1_iir_ref_unit_data_get(fields=fields, max_rows=max_rows, filter=filter, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineryUnitsAndTurnaroundsApi->v1_iir_ref_unit_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|  | [optional] 
 **max_rows** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**FDMAPIDTOV1IIRIIRData**](FDMAPIDTOV1IIRIIRData.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_iir_ref_unit_field_get**
> list[FDMAPIDTOV1IIRIIRField] v1_iir_ref_unit_field_get()



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
api_instance = swagger_client.RefineryUnitsAndTurnaroundsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.v1_iir_ref_unit_field_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineryUnitsAndTurnaroundsApi->v1_iir_ref_unit_field_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FDMAPIDTOV1IIRIIRField]**](FDMAPIDTOV1IIRIIRField.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_iir_ref_unit_field_value_field_name_get**
> list[str] v1_iir_ref_unit_field_value_field_name_get(field_name, filter=filter)



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
api_instance = swagger_client.RefineryUnitsAndTurnaroundsApi(swagger_client.ApiClient(configuration))
field_name = 'field_name_example' # str | 
filter = '' # str |  (optional)

try:
    api_response = api_instance.v1_iir_ref_unit_field_value_field_name_get(field_name, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineryUnitsAndTurnaroundsApi->v1_iir_ref_unit_field_value_field_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

