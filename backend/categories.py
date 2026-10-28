
def get_menu_categories(menu_items):
    """Group menu items by their category."""
    categories = {}

    for item in menu_items:
        category = item.get("category", "Other").strip().title()

        if category not in categories:
            categories[category] = []

        categories[category].append(item)

    return categories


if __name__ == "__main__":
    menu = [
        {"name": "Chicken and Rice", "category": "Meals", "price": 5.00},
        {"name": "Beef Burger", "category": "Meals", "price": 4.50},
        {"name": "Orange Juice", "category": "Drinks", "price": 1.50},
        {"name": "Chocolate Cake", "category": "Desserts", "price": 2.00},
    ]

    result = get_menu_categories(menu)

    for category, items in result.items():
        print(f"\n{category}:")
        for item in items:
            print(f"- {item['name']} (${item['price']:.2f})")
