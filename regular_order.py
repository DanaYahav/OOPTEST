from typing import override
from order import Order

class RegularOrder(Order):

    def __init__(self, order_id, name, delivery_address,items, customer, payment_type, order_date):

        super().__init__(order_id,name,delivery_address,items,customer,payment_type,order_date)



    @override
    def get_order_type(self):
        return "Regular"

    @override
    def calculate_total_price(self):
        total = 0

        for item in self.get_items():
            total += item.get_item_price()

        return total

    from typing import override

    @override
    def __str__(self):
        text = super().__str__()
        text += f"\nFinal Price: {self.get_total_price()}₪"

        return text