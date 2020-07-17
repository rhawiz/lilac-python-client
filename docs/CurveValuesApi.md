# swagger_client.CurveValuesApi

All URIs are relative to *https://sprod1.lilacfdm.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_curve_values_aggregated_curve_id_result_period_type_result_period_length_get**](CurveValuesApi.md#v1_curve_values_aggregated_curve_id_result_period_type_result_period_length_get) | **GET** /v1/CurveValues/Aggregated/{CurveID}/{ResultPeriodType}/{ResultPeriodLength} | 
[**v1_curve_values_curve_id_get**](CurveValuesApi.md#v1_curve_values_curve_id_get) | **GET** /v1/CurveValues/{CurveID} | 
[**v1_curve_values_forecast_curve_id_scenario_id_forecast_date_get**](CurveValuesApi.md#v1_curve_values_forecast_curve_id_scenario_id_forecast_date_get) | **GET** /v1/CurveValues/Forecast/{CurveID}/{ScenarioID}/{ForecastDate} | 
[**v1_curve_values_latest_forecast_curve_id_scenario_id_get**](CurveValuesApi.md#v1_curve_values_latest_forecast_curve_id_scenario_id_get) | **GET** /v1/CurveValues/LatestForecast/{CurveID}/{ScenarioID} | 

# **v1_curve_values_aggregated_curve_id_result_period_type_result_period_length_get**
> list[FDMAPIDTOV1CurveAggregatedValue] v1_curve_values_aggregated_curve_id_result_period_type_result_period_length_get(curve_id, result_period_type, result_period_length, scenario_id=scenario_id, max_forecast_date=max_forecast_date, result_timezone=result_timezone, min_value_date=min_value_date, max_value_date=max_value_date, calculate_proportional=calculate_proportional, exclude_nulls=exclude_nulls, source_is_quantity=source_is_quantity, source_timezone=source_timezone, source_period_type=source_period_type, source_period_length=source_period_length, flatten=flatten)



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
api_instance = swagger_client.CurveValuesApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
result_period_type = 'result_period_type_example' # str | 
result_period_length = 56 # int | 
scenario_id = 56 # int |  (optional)
max_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
result_timezone = 'result_timezone_example' # str |  (optional)
min_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
calculate_proportional = true # bool |  (optional)
exclude_nulls = true # bool |  (optional)
source_is_quantity = true # bool |  (optional)
source_timezone = 'source_timezone_example' # str |  (optional)
source_period_type = 'source_period_type_example' # str |  (optional)
source_period_length = 56 # int |  (optional)
flatten = true # bool |  (optional)

try:
    api_response = api_instance.v1_curve_values_aggregated_curve_id_result_period_type_result_period_length_get(curve_id, result_period_type, result_period_length, scenario_id=scenario_id, max_forecast_date=max_forecast_date, result_timezone=result_timezone, min_value_date=min_value_date, max_value_date=max_value_date, calculate_proportional=calculate_proportional, exclude_nulls=exclude_nulls, source_is_quantity=source_is_quantity, source_timezone=source_timezone, source_period_type=source_period_type, source_period_length=source_period_length, flatten=flatten)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveValuesApi->v1_curve_values_aggregated_curve_id_result_period_type_result_period_length_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **result_period_type** | **str**|  | 
 **result_period_length** | **int**|  | 
 **scenario_id** | **int**|  | [optional] 
 **max_forecast_date** | **datetime**|  | [optional] 
 **result_timezone** | **str**|  | [optional] 
 **min_value_date** | **datetime**|  | [optional] 
 **max_value_date** | **datetime**|  | [optional] 
 **calculate_proportional** | **bool**|  | [optional] 
 **exclude_nulls** | **bool**|  | [optional] 
 **source_is_quantity** | **bool**|  | [optional] 
 **source_timezone** | **str**|  | [optional] 
 **source_period_type** | **str**|  | [optional] 
 **source_period_length** | **int**|  | [optional] 
 **flatten** | **bool**|  | [optional] 

### Return type

[**list[FDMAPIDTOV1CurveAggregatedValue]**](FDMAPIDTOV1CurveAggregatedValue.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_curve_values_curve_id_get**
> list[FDMAPIDTOV1CurveScenarioForecastValue] v1_curve_values_curve_id_get(curve_id, scenario_id=scenario_id, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date, min_value_date=min_value_date, max_value_date=max_value_date, result_timezone=result_timezone)



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
api_instance = swagger_client.CurveValuesApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
scenario_id = 56 # int |  (optional)
min_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_forecast_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
result_timezone = 'result_timezone_example' # str |  (optional)

try:
    api_response = api_instance.v1_curve_values_curve_id_get(curve_id, scenario_id=scenario_id, min_forecast_date=min_forecast_date, max_forecast_date=max_forecast_date, min_value_date=min_value_date, max_value_date=max_value_date, result_timezone=result_timezone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveValuesApi->v1_curve_values_curve_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **scenario_id** | **int**|  | [optional] 
 **min_forecast_date** | **datetime**|  | [optional] 
 **max_forecast_date** | **datetime**|  | [optional] 
 **min_value_date** | **datetime**|  | [optional] 
 **max_value_date** | **datetime**|  | [optional] 
 **result_timezone** | **str**|  | [optional] 

### Return type

[**list[FDMAPIDTOV1CurveScenarioForecastValue]**](FDMAPIDTOV1CurveScenarioForecastValue.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_curve_values_forecast_curve_id_scenario_id_forecast_date_get**
> list[FDMAPIDTOV1CurveValue] v1_curve_values_forecast_curve_id_scenario_id_forecast_date_get(curve_id, scenario_id, forecast_date, min_value_date=min_value_date, max_value_date=max_value_date, result_timezone=result_timezone)



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
api_instance = swagger_client.CurveValuesApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
scenario_id = 56 # int | 
forecast_date = '2013-10-20T19:20:30+01:00' # datetime | 
min_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
result_timezone = 'result_timezone_example' # str |  (optional)

try:
    api_response = api_instance.v1_curve_values_forecast_curve_id_scenario_id_forecast_date_get(curve_id, scenario_id, forecast_date, min_value_date=min_value_date, max_value_date=max_value_date, result_timezone=result_timezone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveValuesApi->v1_curve_values_forecast_curve_id_scenario_id_forecast_date_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **scenario_id** | **int**|  | 
 **forecast_date** | **datetime**|  | 
 **min_value_date** | **datetime**|  | [optional] 
 **max_value_date** | **datetime**|  | [optional] 
 **result_timezone** | **str**|  | [optional] 

### Return type

[**list[FDMAPIDTOV1CurveValue]**](FDMAPIDTOV1CurveValue.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_curve_values_latest_forecast_curve_id_scenario_id_get**
> list[FDMAPIDTOV1CurveValue] v1_curve_values_latest_forecast_curve_id_scenario_id_get(curve_id, scenario_id, as_at_date=as_at_date, min_value_date=min_value_date, max_value_date=max_value_date, result_timezone=result_timezone)



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
api_instance = swagger_client.CurveValuesApi(swagger_client.ApiClient(configuration))
curve_id = 56 # int | 
scenario_id = 56 # int | 
as_at_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_value_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
result_timezone = 'result_timezone_example' # str |  (optional)

try:
    api_response = api_instance.v1_curve_values_latest_forecast_curve_id_scenario_id_get(curve_id, scenario_id, as_at_date=as_at_date, min_value_date=min_value_date, max_value_date=max_value_date, result_timezone=result_timezone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurveValuesApi->v1_curve_values_latest_forecast_curve_id_scenario_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curve_id** | **int**|  | 
 **scenario_id** | **int**|  | 
 **as_at_date** | **datetime**|  | [optional] 
 **min_value_date** | **datetime**|  | [optional] 
 **max_value_date** | **datetime**|  | [optional] 
 **result_timezone** | **str**|  | [optional] 

### Return type

[**list[FDMAPIDTOV1CurveValue]**](FDMAPIDTOV1CurveValue.md)

### Authorization

[apikey-v1](../README.md#apikey-v1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

