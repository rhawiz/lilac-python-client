# coding: utf-8

"""
    FDM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.metadata_api import MetadataApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = api.metadata_api.MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_metadata_curve_id_get(self):
        """Test case for v1_metadata_curve_id_get

        """
        pass

    def test_v1_metadata_register_curve_tag_post(self):
        """Test case for v1_metadata_register_curve_tag_post

        """
        pass

    def test_v1_metadata_register_tag_post(self):
        """Test case for v1_metadata_register_tag_post

        """
        pass

    def test_v1_metadata_search_get(self):
        """Test case for v1_metadata_search_get

        """
        pass

    def test_v1_metadata_tag_types_get(self):
        """Test case for v1_metadata_tag_types_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
