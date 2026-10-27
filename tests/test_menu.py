from backend.menu import get_menu, search_menu


def test_search_finds_chicken_items():
    results = search_menu("chicken")
    assert len(results) == 2
    assert results[0]["item"] == "Rice and Chicken"
    assert results[1]["item"] == "Chicken Sandwich"


def test_search_is_case_insensitive():
    results = search_menu("CHICKEN")
    assert len(results) == 2


def test_search_returns_empty_list_for_no_match():
    results = search_menu("Sushi")
    assert results == []


def test_search_returns_empty_list_for_blank_input():
    results = search_menu("   ")
    assert results == []


def test_get_menu_returns_cafeteria_items():
    menu = get_menu("Main Cafeteria")
    assert "Burger" in menu
    assert menu["Burger"] == 6.00


def test_get_menu_returns_empty_dictionary_for_unknown_cafeteria():
    menu = get_menu("Unknown Cafeteria")
    assert menu == {}
