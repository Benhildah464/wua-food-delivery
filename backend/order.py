# Store orders in memory
orders = {}


class Order:
    def __init__(self, order_id, student_id, items, total_price, status="Pending"):
        self.order_id = order_id
        self.student_id = student_id
        self.items = items
        self.total_price = total_price
        self.status = status


def update_order_status(order_id, new_status):
    if order_id not in orders:
        return "Order not found"

    orders[order_id].status = new_status
    return "Order status updated successfully"