orders = {}


class Order:
    def _init_(self, order_id, student_id, items, total_price, status="Pending"):
        self.order_id = order_id
        self.student_id = student_id
        self.items = items
        self.total_price = total_price
        self.status = status
        orders[order_id] = self


def update_order_status(order_id, new_status):
    order = orders.get(order_id)

    if order is None:
        return "Order not found"

    order.status = new_status
    return f"Order {order_id} status updated to {new_status}"