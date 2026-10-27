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
    """Return the menu for a specific cafeteria."""
    return menus.get(cafeteria_name, {})


def search_menu(search_term):
    """Search for food items across all cafeterias."""

    if not isinstance(search_term, str) or not search_term.strip():
        return []

    results = []
    search_term = search_term.strip().lower()

    for cafeteria_name, food_items in menus.items():
        for food_name, price in food_items.items():
            if search_term in food_name.lower():
                results.append({
                    "cafeteria": cafeteria_name,
                    "item": food_name,
                    "price": price
                })

    return results
