# swagger_client.CurveSummaryApi

All URIs are relative to *https://sprod1.lilacfdm.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_curve_forecast_curve_id_forecast_date_get**](CurveSummaryApi.md#v1_curve_forecast_curve_id_forecast_date_get) | **GET** /v1/CurveForecast/{CurveID}/{ForecastDate} | 
[**v1_curve_forecast_list_curve_id_get**](CurveSummaryApi.md#v1_curve_forecast_list_curve_id_get) | **GET** /v1/CurveForecastList/{CurveID} | 
[**v1_curve_scenario_curve_id_get**](CurveSummaryApi.md#v1_curve_scenario_curve_id_get) | **GET** /v1/CurveScenario/{CurveID} | 
[**v1_curve_summary_forecasts_curve_id_get**](CurveSummaryApi.md#v1_curve_summary_forecasts_curve_id_get) | **GET** /v1/CurveSummary/Forecasts/{CurveID} | 
[**v1_curve_summary_values_curve_id_get**](CurveSummaryApi.md#v1_curve_summary_values_curve_id_get) | **GET** /v1/CurveSummary/Values/{CurveID} | 

# **v1_curve_forecast_curve_id_forecast_date_get**
> FDMAPIDTOV1CurveForecast v1_curve_forecast_curve_id_forecast_date_get(curve_id, forecast_date, min_value_date=min_value_date, max_value_date=max_value_date)



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
api_instance = swagger_client.CurveSummaryApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
forecast_date = '2013-10-20T19:20:30+01:00' # datetime | 
min_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.v1_curve_forecast_curve_id_forecast_date_get(curve_id, forecast_date, min_value_date=min_value_date, max_value_date=max_value_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveSummaryApi->v1_curve_forecast_curve_id_forecast_date_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **forecast_date** | **datetime**|  | 
 **min_value_date** | **datetime**|  | [optional] 
 **max_value_date** | **datetime**|  | [optional] 

### Return type

[**FDMAPIDTOV1CurveForecast**](FDMAPIDTOV1CurveForecast.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_curve_forecast_list_curve_id_get**
> list[FDMAPIDTOV1CurveForecastScenario] v1_curve_forecast_list_curve_id_get(curve_id, scenario_id=scenario_id, min_value_date=min_value_date, max_value_date=max_value_date, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)



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
api_instance = swagger_client.CurveSummaryApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
scenario_id = 56 # int |  (optional)
min_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.v1_curve_forecast_list_curve_id_get(curve_id, scenario_id=scenario_id, min_value_date=min_value_date, max_value_date=max_value_date, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveSummaryApi->v1_curve_forecast_list_curve_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **scenario_id** | **int**|  | [optional] 
 **min_value_date** | **datetime**|  | [optional] 
 **max_value_date** | **datetime**|  | [optional] 
 **min_forecast_date** | **datetime**|  | [optional] 
 **max_forecast_date** | **datetime**|  | [optional] 

### Return type

[**list[FDMAPIDTOV1CurveForecastScenario]**](FDMAPIDTOV1CurveForecastScenario.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_curve_scenario_curve_id_get**
> list[int] v1_curve_scenario_curve_id_get(curve_id, min_value_date=min_value_date, max_value_date=max_value_date, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)



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
api_instance = swagger_client.CurveSummaryApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
min_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.v1_curve_scenario_curve_id_get(curve_id, min_value_date=min_value_date, max_value_date=max_value_date, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveSummaryApi->v1_curve_scenario_curve_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **min_value_date** | **datetime**|  | [optional] 
 **max_value_date** | **datetime**|  | [optional] 
 **min_forecast_date** | **datetime**|  | [optional] 
 **max_forecast_date** | **datetime**|  | [optional] 

### Return type

**list[int]**

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_curve_summary_forecasts_curve_id_get**
> FDMAPIDTOV1CurveForecastSummary v1_curve_summary_forecasts_curve_id_get(curve_id, value_date=value_date, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)



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
api_instance = swagger_client.CurveSummaryApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.v1_curve_summary_forecasts_curve_id_get(curve_id, value_date=value_date, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveSummaryApi->v1_curve_summary_forecasts_curve_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **value_date** | **datetime**|  | [optional] 
 **min_forecast_date** | **datetime**|  | [optional] 
 **max_forecast_date** | **datetime**|  | [optional] 

### Return type

[**FDMAPIDTOV1CurveForecastSummary**](FDMAPIDTOV1CurveForecastSummary.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_curve_summary_values_curve_id_get**
> FDMAPIDTOV1CurveValuesSummary v1_curve_summary_values_curve_id_get(curve_id, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)



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
api_instance = swagger_client.CurveSummaryApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
min_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.v1_curve_summary_values_curve_id_get(curve_id, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveSummaryApi->v1_curve_summary_values_curve_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **min_forecast_date** | **datetime**|  | [optional] 
 **max_forecast_date** | **datetime**|  | [optional] 

### Return type

[**FDMAPIDTOV1CurveValuesSummary**](FDMAPIDTOV1CurveValuesSummary.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

