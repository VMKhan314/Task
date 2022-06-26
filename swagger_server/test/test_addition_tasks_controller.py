# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.shop_unit_statistic_response import ShopUnitStatisticResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdditionTasksController(BaseTestCase):
    """AdditionTasksController integration test stubs"""

    def test_node_id_statistic_get(self):
        """Test case for node_id_statistic_get"""

#        query_string = [('date_start', 'date_start_example'),
#                        ('date_end', 'date_end_example')]

        query_string = [('date_start', "2022-02-01T00:00:00.000Z"),  ('date_end', "2022-02-03T00:00:00.000Z")]

        response = self.client.open(
            '/node/{id}/statistic'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
    """  """

    def test_sales_get(self):
        """Test case for sales_get   """
#        query_string = [('_date', '_date_example')]
        query_string = [('date', "2022-05-28T21:12:01.000Z")]

        response = self.client.open(
            '/sales',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
