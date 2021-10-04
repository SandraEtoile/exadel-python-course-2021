import uuid
import time
from typing import List


class Good:
    def __init__(self, id: uuid.UUID, name, price: int):
        self.id = id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id: uuid.UUID, order_date, client_id, goods: List[Good], price=0):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.price = price

    @property
    def price(self):
        return sum(g.price for g in self.goods)

    @price.setter
    def price(self, value):
        self._price = value


class OrderRepository:
    orders = []

    def add(self, order: Order):
        self.orders.append(order)

    def get(self, order_id: uuid.UUID) -> Order:
        return next((o for o in self.orders if o.order_id == order_id), None)

    def list(self, n_latest: int = None) -> List[Order]:
        if n_latest is None:
            return self.orders
        else:
            return self.orders[-n_latest:]

    def delete(self, order_id):
        self.orders.remove(self.get(order_id))


notebook = Good(uuid.uuid4(), "notebook", 10)
mouse = Good(uuid.uuid4(), "mouse", 5)
headphones = Good(uuid.uuid4(), "headphones", 6)

sasha_order = Order(uuid.uuid4(), time.time(), 1, [notebook, mouse])
alex_order_id = uuid.uuid4()
alex_order = Order(alex_order_id, time.time(), 2, [notebook, mouse, headphones])

order_repository = OrderRepository()

order_repository.add(sasha_order)
order_repository.add(alex_order)

assert order_repository.list() == [sasha_order, alex_order]
assert order_repository.list(1) == [alex_order]
assert order_repository.get(alex_order_id) == alex_order

order_repository.delete(alex_order_id)
assert order_repository.list() == [sasha_order]

