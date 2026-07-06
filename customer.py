from customer_type import CustomerType


class Customer:

    customer_ids = []

    def __init__(self, customer_id, first_name, last_name,
                 email, delivery_address,
                 customer_type, customer_discount=None):

        if customer_id in Customer.customer_ids:
            raise Exception("Customer id already exists")

        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__delivery_address = delivery_address
        self.__customer_type = customer_type
        self.__customer_discount = customer_discount
        self.__favorite_items = []
        self.__customer_gift = None

        Customer.customer_ids.append(customer_id)

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_delivery_address(self):
        return self.__delivery_address

    def get_customer_type(self):
        return self.__customer_type

    def get_customer_discount(self):
        return self.__customer_discount

    def get_favorite_items(self):
        return self.__favorite_items

    def get_customer_gift(self):
        return self.__customer_gift


    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_delivery_address(self, delivery_address):
        self.__delivery_address = delivery_address

    def set_customer_type(self, customer_type):
        self.__customer_type = customer_type

    def set_customer_discount(self, customer_discount):
        self.__customer_discount = customer_discount

    def set_customer_gift(self, gift):
        self.__customer_gift = gift


    def add_favorite_item(self, item):
        for favorite in self.__favorite_items:
            if favorite.get_item_name() == item.get_item_name():
                return
        self.__favorite_items.append(item)

    def remove_favorite_item(self, item_name):
        for item in self.__favorite_items:
            if item.get_item_name() == item_name:
                self.__favorite_items.remove(item)
                return

    def take_gift(self, gift):
        self.__customer_gift = gift
        print(f"{self.get_first_name()} received a gift!")

    def open_gift(self):
        if self.__customer_gift is not None:
            self.__customer_gift.open_gift()
        else:
            print("No gift to open.")