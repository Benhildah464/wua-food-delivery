menus = {
    "Main Cafeteria": {
        "Sadza and Beef": 5.00,
        "Rice and Chicken": 7.50,
        "Burger": 6.00,
        "Chips": 3.00,
        "Vegetable Rice": 4.50
    },
    "Student Cafe": {
        "Chicken Sandwich": 4.00,
        "Pizza Slice": 3.50,
        "Hot Dog": 3.00,
        "Fruit Salad": 2.50,
        "Tea": 1.50
    }
}


def get_menu(cafeteria_name):
    return menus.get(cafeteria_name, {})