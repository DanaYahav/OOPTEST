from typing import override
from order import Order
from customer_type import CustomerType
from vip_order_exception import VipOrderException


class VipOrder(Order):

    VIP_DISCOUNT = 50

    def __init__(self, order_id, name, delivery_address,
                 items, customer, payment_type, order_date):

        super().__init__(
            order_id,
            name,
            delivery_address,
            items,
            customer,
            payment_type,
            order_date
        )

    @override
    def calculate_total_price(self):

        customer = self.get_customer()

        if customer.get_customer_type() != CustomerType.VIP:
            raise VipOrderException("Customer is not VIP")

        total = 0

        for item in self.get_items():
            total += item.get_item_price()

        total -= VipOrder.VIP_DISCOUNT

        return total

    @override
    def get_order_type(self):
        return "VIP"

    @override
    def __str__(self):

        text = super().__str__()
        text += f"\nVIP Discount: {VipOrder.VIP_DISCOUNT}₪"
        text += f"\nFinal Price: {self.get_total_price()}₪"

        return text