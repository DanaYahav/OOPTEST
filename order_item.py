class OrderItem:

    item_ids = []

    def __init__(self, item_id, item_name, item_price):
        if item_id in OrderItem.item_ids:
            raise Exception("Item id already exists")

        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price

        OrderItem.item_ids.append(item_id)

    def get_item_id(self):
        return self.item_id

    def get_item_name(self):
        return self.item_name

    def get_item_price(self):
        return self.item_price

    def __str__(self):
        return f"{self.get_item_name()} - {self.get_item_price()}₪"