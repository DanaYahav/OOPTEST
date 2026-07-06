from order_item import OrderItem
from customer import Customer
from customer_type import CustomerType
from payment_type import PaymentType
from regular_order import RegularOrder
from vip_order import VipOrder
from gift import Gift
from vip_order_exception import VipOrderException


def main():

    item1 = OrderItem(1, "Laptop", 5000)
    item2 = OrderItem(2, "Mouse", 150)
    item3 = OrderItem(3, "Keyboard", 250)

    customer1 = Customer(1,"Dana","Yahav","dana@gmail.com","Tel Aviv",CustomerType.REGULAR)
    customer2 = Customer(2,"Noa","Levi","noa@gmail.com","Haifa",CustomerType.VIP,10)

    gift = Gift()
    customer2.take_gift(gift)

    regular_order = RegularOrder(1,"Office Equipment","Tel Aviv",[item1, item2],customer1,PaymentType.CREDIT_CARD,"05/07/2026")
    vip_order = VipOrder(2,"Gaming Accessories","Haifa",[item2, item3],customer2,PaymentType.CASH,"06/07/2026")


    print("========== ORDER ==========")
    print(regular_order)

    print("\nFavorite Items:")
    for item in customer1.get_favorite_items():
        print(f"- {item.get_item_name()} : {item.get_item_price()}₪")

    print("\nOpening Gift:")
    customer1.open_gift()

    print("\n========== ORDER ==========")
    print(vip_order)

    print("\nFavorite Items:")
    for item in customer2.get_favorite_items():
        print(f"- {item.get_item_name()} : {item.get_item_price()}₪")

    print("\nOpening Gift:")
    customer2.open_gift()

    print("\n==================")
    print("\nTrying to create VIP order for regular customer:")

    try:
        wrong_order = VipOrder(3,"Invalid VIP Order","Jerusalem",[item1],customer1,PaymentType.CASH,"02/07/2026")

    except VipOrderException as e:
        print(e)


if __name__ == "__main__":
    main()