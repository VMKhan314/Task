# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.shop_unit import ShopUnit  # noqa: E501
from swagger_server.models.shop_unit_import_request import ShopUnitImportRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBasicTasksController(BaseTestCase):
    """BasicTasksController integration test stubs"""

    def test_delete_id_delete(self):
        """Test case for delete_id_delete

        
        """
        response = self.client.open(
            '/delete/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_imports_post(self):
        """Test case for imports_post

        
        """
        body = ShopUnitImportRequest()
        response = self.client.open(
            '/imports',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_nodes_id_get(self):
        """Test case for nodes_id_get

        
        """
        response = self.client.open(
            '/nodes/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
