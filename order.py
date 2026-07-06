from abc import ABC, abstractmethod
from duplicate_order_exception import DuplicateOrderException
class Order(ABC):

    order_ids = []

    def __init__(self, order_id, name, delivery_address, items, customer, payment_type, order_date):

        if order_id in Order.order_ids:
            raise DuplicateOrderException("Order id already exists")

        self.__order_id = order_id
        self.__name = name
        self.__delivery_address = delivery_address
        self.__items = items
        self.__customer = customer
        self.__payment_type = payment_type
        self.__order_date = order_date
        for item in items:
            customer.add_favorite_item(item)

        Order.order_ids.append(order_id)

        self.__total_price = self.calculate_total_price()

    def __str__(self):

        text = f"Order Type: {self.get_order_type()}\n"
        text += f"Order ID: {self.get_order_id()}\n"
        text += f"Order Name: {self.get_name()}\n"
        text += f"Customer: {self.get_customer().get_first_name()} {self.get_customer().get_last_name()}\n"
        text += f"Delivery Address: {self.get_delivery_address()}\n"
        text += f"Payment Type: {self.get_payment_type().name}\n"
        text += f"Order Date: {self.get_order_date()}\n"

        text += "\nItems:\n"

        for item in self.get_items():
            text += f"   • {item.get_item_name()} - {item.get_item_price()}₪\n"

        return text


    def get_order_id(self):
        return self.__order_id

    def get_name(self):
        return self.__name

    def get_delivery_address(self):
        return self.__delivery_address

    def get_items(self):
        return self.__items

    def get_customer(self):
        return self.__customer

    def get_payment_type(self):
        return self.__payment_type

    def get_order_date(self):
        return self.__order_date

    def get_total_price(self):
        return self.__total_price

    def set_name(self, name):
        self.__name = name

    def set_delivery_address(self, delivery_address):
        self.__delivery_address = delivery_address

    def set_items(self, items):
        self.__items = items

    def set_customer(self, customer):
        self.__customer = customer

    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type

    def set_order_date(self, order_date):
        self.__order_date = order_date


    @abstractmethod
    def calculate_total_price(self):
        pass