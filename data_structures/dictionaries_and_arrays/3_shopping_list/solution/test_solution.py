def test_solution():
    from solution import cheapest_store

    grocery_dict1 = {"Walmart": {"pasta": 2.0,
                                "bread": 1.5,
                                "cheese": 6.0,
                                "ketchup": 3.0,
                                "salami": 9.0,
                                "onions": 1.0},
                    "Thriftys": {"bread": 4.0,
                                "ham": 6.0,
                                "salami": 12.0,
                                "pasta": 1.75,
                                "mayo": 4.0,
                                "onions": 2.0,
                                "ketchup": 3.5}
                    }

    shopping_list1 = ["ham", "salami", "ketchup", "mayo", "pasta", "cheese", "tuna"]
    
    assert cheapest_store(grocery_dict1, shopping_list1) == "Walmart"

    grocery_dict2 = {"Whole Foods": {"fish": 5.0,
                                     "meat": 6.0,
                                     "waffles": 3.0}
                    }
    shopping_list2 = ["fish", "bread"]
    assert cheapest_store(grocery_dict2, shopping_list2) == "Whole Foods"

    grocery_dict3 = {"Whole Foods": {"fish": 5.0,
                                     "meat": 6.0,
                                     "waffles": 3.0},
                     "Walmart": {"fish": 5.0,
                                 "bread": 2.0}
                    }
    assert cheapest_store(grocery_dict3, ["pasta", "cheese"]) == "Walmart"
