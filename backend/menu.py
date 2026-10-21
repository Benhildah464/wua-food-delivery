cafeteria_menus = {
    "Main Cafeteria": {
        "Sadza and Beef": 5.00,
        "Rice and Chicken": 6.00,
        "Beef Burger": 4.50,
        "Chips": 2.50,
        "Sandwich": 3.00
    },
    "Student Cafeteria": {
        "Sadza and Vegetables": 3.00,
        "Rice and Beans": 3.50,
        "Chicken Pie": 2.00,
        "Hot Dog": 2.50,
        "Tea": 1.00
    }
}


def get_menu(cafeteria_name):
    return cafeteria_menus.get(cafeteria_name, "Cafeteria not found")
