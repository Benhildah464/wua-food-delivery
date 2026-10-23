orders = {}

# Allowed order statuses
ALLOWED_STATUSES = [
    "Pending",
    "Preparing",
    "Ready for Delivery",
    "Delivered"
]


class Order:
    """Represent a cafeteria food order."""

    def _init_(self, order_id, student_id, items, total_price,
                 status="Pending"):
        """Create an order after validating its details."""

        if not order_id or not student_id:
            raise ValueError("Order ID and student ID are required")

        if not isinstance(items, list) or not items:
            raise ValueError("Order items must be a non-empty list")

        if not isinstance(total_price, (int, float)) or total_price < 0:
            raise ValueError("Total price must be a non-negative number")

        if status not in ALLOWED_STATUSES:
            raise ValueError("Invalid order status")

        self.order_id = order_id
        self.student_id = student_id
        self.items = items
        self.total_price = total_price
        self.status = status

        orders[order_id] = self


def update_order_status(order_id, new_status):
    """Update an order's status and return a result message."""

    order = orders.get(order_id)

    if order is None:
        return "Order not found"

    if new_status not in ALLOWED_STATUSES:
        return "Invalid order status"

    order.status = new_status
    return f"Order {order_id} status updated to {new_status}"