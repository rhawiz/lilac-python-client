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


class FDMAPIDTOV1CrudesCrudesGrade(object):
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
        'refinery_code': 'str',
        'sulphur_low': 'float',
        'sulphur_medium': 'float',
        'sulphur_high': 'float',
        'grade_extra_light': 'float',
        'grade_light': 'float',
        'grade_medium': 'float',
        'grade_heavy': 'float',
        'grade_extra_heavy': 'float',
        'source': 'str',
        'last_updated': 'datetime'
    }

    attribute_map = {
        'refinery_code': 'refineryCode',
        'sulphur_low': 'sulphurLow',
        'sulphur_medium': 'sulphurMedium',
        'sulphur_high': 'sulphurHigh',
        'grade_extra_light': 'gradeExtraLight',
        'grade_light': 'gradeLight',
        'grade_medium': 'gradeMedium',
        'grade_heavy': 'gradeHeavy',
        'grade_extra_heavy': 'gradeExtraHeavy',
        'source': 'source',
        'last_updated': 'lastUpdated'
    }

    def __init__(self, refinery_code=None, sulphur_low=None, sulphur_medium=None, sulphur_high=None, grade_extra_light=None, grade_light=None, grade_medium=None, grade_heavy=None, grade_extra_heavy=None, source=None, last_updated=None):  # noqa: E501
        """FDMAPIDTOV1CrudesCrudesGrade - a model defined in Swagger"""  # noqa: E501
        self._refinery_code = None
        self._sulphur_low = None
        self._sulphur_medium = None
        self._sulphur_high = None
        self._grade_extra_light = None
        self._grade_light = None
        self._grade_medium = None
        self._grade_heavy = None
        self._grade_extra_heavy = None
        self._source = None
        self._last_updated = None
        self.discriminator = None
        if refinery_code is not None:
            self.refinery_code = refinery_code
        if sulphur_low is not None:
            self.sulphur_low = sulphur_low
        if sulphur_medium is not None:
            self.sulphur_medium = sulphur_medium
        if sulphur_high is not None:
            self.sulphur_high = sulphur_high
        if grade_extra_light is not None:
            self.grade_extra_light = grade_extra_light
        if grade_light is not None:
            self.grade_light = grade_light
        if grade_medium is not None:
            self.grade_medium = grade_medium
        if grade_heavy is not None:
            self.grade_heavy = grade_heavy
        if grade_extra_heavy is not None:
            self.grade_extra_heavy = grade_extra_heavy
        if source is not None:
            self.source = source
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def refinery_code(self):
        """Gets the refinery_code of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The refinery_code of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: str
        """
        return self._refinery_code

    @refinery_code.setter
    def refinery_code(self, refinery_code):
        """Sets the refinery_code of this FDMAPIDTOV1CrudesCrudesGrade.


        :param refinery_code: The refinery_code of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: str
        """

        self._refinery_code = refinery_code

    @property
    def sulphur_low(self):
        """Gets the sulphur_low of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The sulphur_low of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._sulphur_low

    @sulphur_low.setter
    def sulphur_low(self, sulphur_low):
        """Sets the sulphur_low of this FDMAPIDTOV1CrudesCrudesGrade.


        :param sulphur_low: The sulphur_low of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._sulphur_low = sulphur_low

    @property
    def sulphur_medium(self):
        """Gets the sulphur_medium of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The sulphur_medium of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._sulphur_medium

    @sulphur_medium.setter
    def sulphur_medium(self, sulphur_medium):
        """Sets the sulphur_medium of this FDMAPIDTOV1CrudesCrudesGrade.


        :param sulphur_medium: The sulphur_medium of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._sulphur_medium = sulphur_medium

    @property
    def sulphur_high(self):
        """Gets the sulphur_high of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The sulphur_high of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._sulphur_high

    @sulphur_high.setter
    def sulphur_high(self, sulphur_high):
        """Sets the sulphur_high of this FDMAPIDTOV1CrudesCrudesGrade.


        :param sulphur_high: The sulphur_high of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._sulphur_high = sulphur_high

    @property
    def grade_extra_light(self):
        """Gets the grade_extra_light of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The grade_extra_light of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._grade_extra_light

    @grade_extra_light.setter
    def grade_extra_light(self, grade_extra_light):
        """Sets the grade_extra_light of this FDMAPIDTOV1CrudesCrudesGrade.


        :param grade_extra_light: The grade_extra_light of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._grade_extra_light = grade_extra_light

    @property
    def grade_light(self):
        """Gets the grade_light of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The grade_light of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._grade_light

    @grade_light.setter
    def grade_light(self, grade_light):
        """Sets the grade_light of this FDMAPIDTOV1CrudesCrudesGrade.


        :param grade_light: The grade_light of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._grade_light = grade_light

    @property
    def grade_medium(self):
        """Gets the grade_medium of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The grade_medium of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._grade_medium

    @grade_medium.setter
    def grade_medium(self, grade_medium):
        """Sets the grade_medium of this FDMAPIDTOV1CrudesCrudesGrade.


        :param grade_medium: The grade_medium of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._grade_medium = grade_medium

    @property
    def grade_heavy(self):
        """Gets the grade_heavy of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The grade_heavy of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._grade_heavy

    @grade_heavy.setter
    def grade_heavy(self, grade_heavy):
        """Sets the grade_heavy of this FDMAPIDTOV1CrudesCrudesGrade.


        :param grade_heavy: The grade_heavy of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._grade_heavy = grade_heavy

    @property
    def grade_extra_heavy(self):
        """Gets the grade_extra_heavy of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The grade_extra_heavy of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: float
        """
        return self._grade_extra_heavy

    @grade_extra_heavy.setter
    def grade_extra_heavy(self, grade_extra_heavy):
        """Sets the grade_extra_heavy of this FDMAPIDTOV1CrudesCrudesGrade.


        :param grade_extra_heavy: The grade_extra_heavy of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: float
        """

        self._grade_extra_heavy = grade_extra_heavy

    @property
    def source(self):
        """Gets the source of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The source of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this FDMAPIDTOV1CrudesCrudesGrade.


        :param source: The source of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def last_updated(self):
        """Gets the last_updated of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501


        :return: The last_updated of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this FDMAPIDTOV1CrudesCrudesGrade.


        :param last_updated: The last_updated of this FDMAPIDTOV1CrudesCrudesGrade.  # noqa: E501
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
        if issubclass(FDMAPIDTOV1CrudesCrudesGrade, dict):
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
        if not isinstance(other, FDMAPIDTOV1CrudesCrudesGrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
