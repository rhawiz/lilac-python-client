# coding: utf-8

"""
    FDM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FDMAPIDTOV1CurveImport(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'curve_id': 'int',
        'scenario_id': 'int',
        'forecast_date': 'datetime',
        'values': 'list[FDMAPIDTOV1CurveValue]'
    }

    attribute_map = {
        'curve_id': 'curveID',
        'scenario_id': 'scenarioID',
        'forecast_date': 'forecastDate',
        'values': 'values'
    }

    def __init__(self, curve_id=None, scenario_id=None, forecast_date=None, values=None):  # noqa: E501
        """FDMAPIDTOV1CurveImport - a model defined in Swagger"""  # noqa: E501
        self._curve_id = None
        self._scenario_id = None
        self._forecast_date = None
        self._values = None
        self.discriminator = None
        if curve_id is not None:
            self.curve_id = curve_id
        if scenario_id is not None:
            self.scenario_id = scenario_id
        if forecast_date is not None:
            self.forecast_date = forecast_date
        if values is not None:
            self.values = values

    @property
    def curve_id(self):
        """Gets the curve_id of this FDMAPIDTOV1CurveImport.  # noqa: E501


        :return: The curve_id of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :rtype: int
        """
        return self._curve_id

    @curve_id.setter
    def curve_id(self, curve_id):
        """Sets the curve_id of this FDMAPIDTOV1CurveImport.


        :param curve_id: The curve_id of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :type: int
        """

        self._curve_id = curve_id

    @property
    def scenario_id(self):
        """Gets the scenario_id of this FDMAPIDTOV1CurveImport.  # noqa: E501


        :return: The scenario_id of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :rtype: int
        """
        return self._scenario_id

    @scenario_id.setter
    def scenario_id(self, scenario_id):
        """Sets the scenario_id of this FDMAPIDTOV1CurveImport.


        :param scenario_id: The scenario_id of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :type: int
        """

        self._scenario_id = scenario_id

    @property
    def forecast_date(self):
        """Gets the forecast_date of this FDMAPIDTOV1CurveImport.  # noqa: E501


        :return: The forecast_date of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :rtype: datetime
        """
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, forecast_date):
        """Sets the forecast_date of this FDMAPIDTOV1CurveImport.


        :param forecast_date: The forecast_date of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :type: datetime
        """

        self._forecast_date = forecast_date

    @property
    def values(self):
        """Gets the values of this FDMAPIDTOV1CurveImport.  # noqa: E501


        :return: The values of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :rtype: list[FDMAPIDTOV1CurveValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this FDMAPIDTOV1CurveImport.


        :param values: The values of this FDMAPIDTOV1CurveImport.  # noqa: E501
        :type: list[FDMAPIDTOV1CurveValue]
        """

        self._values = values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FDMAPIDTOV1CurveImport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FDMAPIDTOV1CurveImport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other