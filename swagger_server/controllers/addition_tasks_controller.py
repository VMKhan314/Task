import connexion
import six
from swagger_server.controllers.services import *

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.shop_unit_statistic_response import ShopUnitStatisticResponse  # noqa: E501
from swagger_server import util


def node_id_statistic_get(id, date_start=None, date_end=None):  # noqa: E501
    """node_id_statistic_get

    Получение статистики (истории обновлений) по товару/категории за заданный полуинтервал [from, to). Статистика по удаленным элементам недоступна.  - цена категории - это средняя цена всех её товаров, включая товары дочерних категорий.Если категория не содержит товаров цена равна null. При обновлении цены товара, средняя цена категории, которая содержит этот товар, тоже обновляется. - можно получить статистику за всё время.  # noqa: E501

    :param id: UUID товара/категории для которой будет отображаться статистика
    :type id: 
    :param date_start: Дата и время начала интервала, для которого считается статистика. Дата должна обрабатываться согласно ISO 8601 (такой придерживается OpenAPI). Если дата не удовлетворяет данному формату, необходимо отвечать 400.
    :type date_start: str
    :param date_end: Дата и время конца интервала, для которого считается статистика. Дата должна обрабатываться согласно ISO 8601 (такой придерживается OpenAPI). Если дата не удовлетворяет данному формату, необходимо отвечать 400.
    :type date_end: str

    :rtype: ShopUnitStatisticResponse
    """
    d ={
        "items": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66a444",
                "name": "Оффер",
                "date": "2022-05-28T21:12:01.000Z",
                "parentId": "3fa85f64-5717-4562-b3fc-2c963f66a333",
                "price": 234,
                "type": "OFFER"
            }
        ]
    }
    return ShopUnitStatisticResponse.from_dict(d)


def sales_get(date):  # noqa: E501
    """sales_get

    Получение списка **товаров**, цена которых была обновлена за последние 24 часа включительно [now() - 24h, now()] от времени переданном в запросе.
    Обновление цены не означает её изменение. Обновления цен удаленных товаров недоступны.
    При обновлении цены товара, средняя цена категории, которая содержит этот товар, тоже обновляется.  # noqa: E501

    :param _date: Дата и время запроса. Дата должна обрабатываться согласно ISO 8601 (такой придерживается OpenAPI).
    Если дата не удовлетворяет данному формату, необходимо отвечать 400
    :type _date: str

    :rtype: ShopUnitStatisticResponse
    """
    d =database.sales(date)

    if d!=None:
        return d
    else:
        return ({
                  "code": 400,
                  "message": "Validation Failed"
                }, 400)
