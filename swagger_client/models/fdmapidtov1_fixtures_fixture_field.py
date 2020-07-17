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


class FDMAPIDTOV1FixturesFixtureField(object):
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
        'fixture_type_name': 'str',
        'field_name': 'str',
        'data_type_name': 'str',
        'order_id': 'int',
        'display_name': 'str'
    }

    attribute_map = {
        'fixture_type_name': 'fixtureTypeName',
        'field_name': 'fieldName',
        'data_type_name': 'dataTypeName',
        'order_id': 'orderID',
        'display_name': 'displayName'
    }

    def __init__(self, fixture_type_name=None, field_name=None, data_type_name=None, order_id=None, display_name=None):  # noqa: E501
        """FDMAPIDTOV1FixturesFixtureField - a model defined in Swagger"""  # noqa: E501
        self._fixture_type_name = None
        self._field_name = None
        self._data_type_name = None
        self._order_id = None
        self._display_name = None
        self.discriminator = None
        if fixture_type_name is not None:
            self.fixture_type_name = fixture_type_name
        if field_name is not None:
            self.field_name = field_name
        if data_type_name is not None:
            self.data_type_name = data_type_name
        if order_id is not None:
            self.order_id = order_id
        if display_name is not None:
            self.display_name = display_name

    @property
    def fixture_type_name(self):
        """Gets the fixture_type_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501


        :return: The fixture_type_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :rtype: str
        """
        return self._fixture_type_name

    @fixture_type_name.setter
    def fixture_type_name(self, fixture_type_name):
        """Sets the fixture_type_name of this FDMAPIDTOV1FixturesFixtureField.


        :param fixture_type_name: The fixture_type_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :type: str
        """

        self._fixture_type_name = fixture_type_name

    @property
    def field_name(self):
        """Gets the field_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501


        :return: The field_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this FDMAPIDTOV1FixturesFixtureField.


        :param field_name: The field_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

    @property
    def data_type_name(self):
        """Gets the data_type_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501


        :return: The data_type_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :rtype: str
        """
        return self._data_type_name

    @data_type_name.setter
    def data_type_name(self, data_type_name):
        """Sets the data_type_name of this FDMAPIDTOV1FixturesFixtureField.


        :param data_type_name: The data_type_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :type: str
        """

        self._data_type_name = data_type_name

    @property
    def order_id(self):
        """Gets the order_id of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501


        :return: The order_id of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this FDMAPIDTOV1FixturesFixtureField.


        :param order_id: The order_id of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def display_name(self):
        """Gets the display_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501


        :return: The display_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FDMAPIDTOV1FixturesFixtureField.


        :param display_name: The display_name of this FDMAPIDTOV1FixturesFixtureField.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if issubclass(FDMAPIDTOV1FixturesFixtureField, dict):
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
        if not isinstance(other, FDMAPIDTOV1FixturesFixtureField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
