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


class FDMAPIDTOV1CrudesCrudesMeta(object):
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
        'crude_id': 'str',
        'crude_name': 'str',
        'api': 'float',
        'sulphur': 'float',
        'tan': 'float',
        'source': 'str',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'crude_id': 'crudeID',
        'crude_name': 'crudeName',
        'api': 'api',
        'sulphur': 'sulphur',
        'tan': 'tan',
        'source': 'source',
        'last_updated': 'lastUpdated'
    }

    def __init__(self, crude_id=None, crude_name=None, api=None, sulphur=None, tan=None, source=None, last_updated=None):  # noqa: E501
        """FDMAPIDTOV1CrudesCrudesMeta - a model defined in Swagger"""  # noqa: E501
        self._crude_id = None
        self._crude_name = None
        self._api = None
        self._sulphur = None
        self._tan = None
        self._source = None
        self._last_updated = None
        self.discriminator = None
        if crude_id is not None:
            self.crude_id = crude_id
        if crude_name is not None:
            self.crude_name = crude_name
        if api is not None:
            self.api = api
        if sulphur is not None:
            self.sulphur = sulphur
        if tan is not None:
            self.tan = tan
        if source is not None:
            self.source = source
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def crude_id(self):
        """Gets the crude_id of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501


        :return: The crude_id of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :rtype: str
        """
        return self._crude_id

    @crude_id.setter
    def crude_id(self, crude_id):
        """Sets the crude_id of this FDMAPIDTOV1CrudesCrudesMeta.


        :param crude_id: The crude_id of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :type: str
        """

        self._crude_id = crude_id

    @property
    def crude_name(self):
        """Gets the crude_name of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501


        :return: The crude_name of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :rtype: str
        """
        return self._crude_name

    @crude_name.setter
    def crude_name(self, crude_name):
        """Sets the crude_name of this FDMAPIDTOV1CrudesCrudesMeta.


        :param crude_name: The crude_name of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :type: str
        """

        self._crude_name = crude_name

    @property
    def api(self):
        """Gets the api of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501


        :return: The api of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :rtype: float
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this FDMAPIDTOV1CrudesCrudesMeta.


        :param api: The api of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :type: float
        """

        self._api = api

    @property
    def sulphur(self):
        """Gets the sulphur of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501


        :return: The sulphur of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :rtype: float
        """
        return self._sulphur

    @sulphur.setter
    def sulphur(self, sulphur):
        """Sets the sulphur of this FDMAPIDTOV1CrudesCrudesMeta.


        :param sulphur: The sulphur of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :type: float
        """

        self._sulphur = sulphur

    @property
    def tan(self):
        """Gets the tan of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501


        :return: The tan of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :rtype: float
        """
        return self._tan

    @tan.setter
    def tan(self, tan):
        """Sets the tan of this FDMAPIDTOV1CrudesCrudesMeta.


        :param tan: The tan of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :type: float
        """

        self._tan = tan

    @property
    def source(self):
        """Gets the source of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501


        :return: The source of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this FDMAPIDTOV1CrudesCrudesMeta.


        :param source: The source of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def last_updated(self):
        """Gets the last_updated of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501


        :return: The last_updated of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this FDMAPIDTOV1CrudesCrudesMeta.


        :param last_updated: The last_updated of this FDMAPIDTOV1CrudesCrudesMeta.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

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
        if issubclass(FDMAPIDTOV1CrudesCrudesMeta, dict):
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
        if not isinstance(other, FDMAPIDTOV1CrudesCrudesMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
