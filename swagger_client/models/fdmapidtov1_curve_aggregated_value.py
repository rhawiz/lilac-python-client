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


class FDMAPIDTOV1CurveAggregatedValue(object):
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
        'value_date': 'datetime',
        'value_end_date': 'datetime',
        'value': 'float'
    }

    attribute_map = {
        'value_date': 'valueDate',
        'value_end_date': 'valueEndDate',
        'value': 'value'
    }

    def __init__(self, value_date=None, value_end_date=None, value=None):  # noqa: E501
        """FDMAPIDTOV1CurveAggregatedValue - a model defined in Swagger"""  # noqa: E501
        self._value_date = None
        self._value_end_date = None
        self._value = None
        self.discriminator = None
        if value_date is not None:
            self.value_date = value_date
        if value_end_date is not None:
            self.value_end_date = value_end_date
        if value is not None:
            self.value = value

    @property
    def value_date(self):
        """Gets the value_date of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501


        :return: The value_date of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501
        :rtype: datetime
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this FDMAPIDTOV1CurveAggregatedValue.


        :param value_date: The value_date of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501
        :type: datetime
        """

        self._value_date = value_date

    @property
    def value_end_date(self):
        """Gets the value_end_date of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501


        :return: The value_end_date of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501
        :rtype: datetime
        """
        return self._value_end_date

    @value_end_date.setter
    def value_end_date(self, value_end_date):
        """Sets the value_end_date of this FDMAPIDTOV1CurveAggregatedValue.


        :param value_end_date: The value_end_date of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501
        :type: datetime
        """

        self._value_end_date = value_end_date

    @property
    def value(self):
        """Gets the value of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501


        :return: The value of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FDMAPIDTOV1CurveAggregatedValue.


        :param value: The value of this FDMAPIDTOV1CurveAggregatedValue.  # noqa: E501
        :type: float
        """

        self._value = value

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
        if issubclass(FDMAPIDTOV1CurveAggregatedValue, dict):
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
        if not isinstance(other, FDMAPIDTOV1CurveAggregatedValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
