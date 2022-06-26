import os.path
import pickle
from datetime import datetime
import dateutil.parser as dp


def ShopUnit_(_id: str = None, name: str = None, date: str = None,
              parent_id: str = None, _type: str = None, price: int = None,
              children: [] = None):
    return {
        'id': _id,
        'name': name,
        'date': date,
        'parentId': parent_id,
        'type': _type,
        'price': price,
        'children': children
    }


class ind():
    pass


ind.id, ind.name, ind.parent_id, ind.type, ind.price, ind.updateDate = range(6)


class services():
    def __init__(self, basepath='/data/db.pickle'):
        self.basepath = basepath

        if os.path.exists(basepath):
            with open(basepath, "rb") as fp: 
                self.data = pickle.load(fp)
        else:
            self.data = ([], {})
            path = '/'.join(basepath.split('/')[0:-1])
            if not os.path.exists(path):
                # Create a new directory because it does not exist
                os.makedirs(path)

    def save(self):
        with open(self.basepath, "wb") as fp:  
            pickle.dump(self.data, fp)

    def reset(self):
        self.data = ([], {})
        self.save()

    def delete_objects(self, id_):
        data_list, data_dict = self.data

        if id_ not in data_dict:
            # return (Error(404,'Item not found'), 404)
            return False
        res = set()  # []  # список для удаления set!!!
        arr = set([data_dict[id_]])

        for i, item in enumerate(data_list):
            if item[ind.id] == id_:
                res.add(i)
        while len(arr) > 0:
            v = arr.pop()
            for i, item in enumerate(data_list):
                if item[ind.parent_id] == data_list[v][ind.id]:
                    arr.add(i)
            res.add(v)

        res = sorted(list(res))
        # удаление с конца
        for i in res[::-1]:
            del data_list[i]
        # словарь ссылок заново
        data_dict.clear()
        for i, item in enumerate(data_list):
            data_dict[item[ind.id]] = i
        self.save()
        return True

    def import_objects(self, body):
        updateDate = body._update_date

        data_list, data_dict = self.data

        for shop in body._items:
            data_dict[shop.id] = len(data_list)
            data_list.append([shop.id, shop.name, shop.parent_id,
                              shop.type, shop.price, updateDate])
        self.save()

    def fun(self, istart, level=0):
        data_list, data_dict = self.data

        maxtime = 0

        children = []
        arr2 = []  # индексы для отладки

        n = summ = 0
        for j in data_dict:
            i = data_dict[j]
            item = data_list[i]
            if item[ind.parent_id] == data_list[istart][ind.id]:
                res, arr1, n1, summ1, time = self.fun(i, level + 1)
                maxtime = max(maxtime, time)
                arr2 += arr1
                n += n1
                summ += summ1
                children.append(res)
        arr = [istart]
        if len(arr2) > 0:
            arr.append(arr2)
        else:
            price = data_list[istart][ind.price]
            if price != None:
                n = 1
                summ = price
            else:
                n = 0
                summ = 0
        if len(children) == 0:
            children = None

        item = data_list[istart]
        time = int(dp.parse(item[ind.updateDate]).timestamp())
        maxtime = max(maxtime, time)
        res = ShopUnit_(item[ind.id], item[ind.name], item[ind.updateDate],
                        item[ind.parent_id], item[ind.type], item[ind.price],
                        children)

        if children != None:
            res['price'] = summ // n
            res['date'] = datetime.utcfromtimestamp(
                maxtime).isoformat() + ".000Z"

        return res, arr, n, summ, maxtime

    def node_objects(self, id_):
        data_list, data_dict = self.data

        if id_ not in data_dict:
            return None  # (Error(404,'Item not found'), 404)
        else:
            istart = data_dict[id_]
        res, arr, n, summ, time = self.fun(istart)
        return res

    def sales(self, date):
        data_list, data_dict = self.data
        try:
            parsed_t = dp.parse(date)
        except Exception as e:
            return None

        t_end = int(parsed_t.timestamp())
        t_begin = t_end - 24 * 3600  # на сутки ранее

        res = []  # список
        for i in data_dict.values():
            s = data_list[i]
            parsed_t = dp.parse(s[ind.updateDate])
            t_in_seconds = int(parsed_t.timestamp())

            if t_begin <= t_in_seconds <= t_end and s[ind.type] == "OFFER":
                res.append({
                    "id": s[ind.id],
                    "name": s[ind.name],
                    "date": s[ind.updateDate],
                    "parentId": s[ind.parent_id],
                    "price": s[ind.price],
                    "type": s[ind.type]
                })
        if len(res) == 0:
            res = None
        return {"items": res}


# путь от корня basepath = '/data/db.pickle'
database = services()