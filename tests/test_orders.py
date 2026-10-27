import pytest

from backend.order import Order, orders, update_order_status


@pytest.fixture(autouse=True)
def clear_orders():
    orders.clear()


def test_create_valid_order():
    order = Order("ORD001", "STU001", ["Burger"], 5.00)
    assert order.order_id == "ORD001"
    assert order.student_id == "STU001"
    assert order.items == ["Burger"]
    assert order.total_price == 5.00
    assert order.status == "Pending"


def test_reject_empty_order_id():
    with pytest.raises(ValueError):
        Order("", "STU001", ["Burger"], 5.00)


def test_reject_empty_student_id():
    with pytest.raises(ValueError):
        Order("ORD001", "", ["Burger"], 5.00)


def test_reject_empty_items():
    with pytest.raises(ValueError):
        Order("ORD001", "STU001", [], 5.00)


def test_reject_negative_price():
    with pytest.raises(ValueError):
        Order("ORD001", "STU001", ["Burger"], -5.00)


def test_reject_invalid_status():
    with pytest.raises(ValueError):
        Order("ORD001", "STU001", ["Burger"], 5.00, "Unknown")


def test_update_order_status():
    Order("ORD001", "STU001", ["Burger"], 5.00)
    result = update_order_status("ORD001", "Preparing")
    assert result == "Order ORD001 status updated to Preparing"
    assert orders["ORD001"].status == "Preparing"


def test_update_nonexistent_order():
    result = update_order_status("UNKNOWN", "Preparing")
    assert result == "Order not found"
