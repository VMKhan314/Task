# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.shop_unit_import import ShopUnitImport  # noqa: F401,E501
from swagger_server import util


class ShopUnitImportRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, items: List[ShopUnitImport]=None, update_date: str=None):  # noqa: E501
        """ShopUnitImportRequest - a model defined in Swagger

        :param items: The items of this ShopUnitImportRequest.  # noqa: E501
        :type items: List[ShopUnitImport]
        :param update_date: The update_date of this ShopUnitImportRequest.  # noqa: E501
        :type update_date: str
        """
        self.swagger_types = {
            'items': List[ShopUnitImport],
            'update_date': str
        }

        self.attribute_map = {
            'items': 'items',
            'update_date': 'updateDate'
        }
        self._items = items
        self._update_date = update_date

    @classmethod
    def from_dict(cls, dikt) -> 'ShopUnitImportRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ShopUnitImportRequest of this ShopUnitImportRequest.  # noqa: E501
        :rtype: ShopUnitImportRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def items(self) -> List[ShopUnitImport]:
        """Gets the items of this ShopUnitImportRequest.

        Импортируемые элементы  # noqa: E501

        :return: The items of this ShopUnitImportRequest.
        :rtype: List[ShopUnitImport]
        """
        return self._items

    @items.setter
    def items(self, items: List[ShopUnitImport]):
        """Sets the items of this ShopUnitImportRequest.

        Импортируемые элементы  # noqa: E501

        :param items: The items of this ShopUnitImportRequest.
        :type items: List[ShopUnitImport]
        """

        self._items = items

    @property
    def update_date(self) -> str:
        """Gets the update_date of this ShopUnitImportRequest.

        Время обновления добавляемых товаров/категорий.  # noqa: E501

        :return: The update_date of this ShopUnitImportRequest.
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date: str):
        """Sets the update_date of this ShopUnitImportRequest.

        Время обновления добавляемых товаров/категорий.  # noqa: E501

        :param update_date: The update_date of this ShopUnitImportRequest.
        :type update_date: str
        """

        self._update_date = update_date
