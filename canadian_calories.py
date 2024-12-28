burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

menu = {
    "burger_options" : {
        1: {
            "name": "cheeseburger",
            "calories": 461
        },
        2: {
            "name": "Fish Burger",
            "calories": 431
        },
        3: {
            "name": "Veggie Burger",
            "calories": 420
        },
        4: {
            "name": "No Burger",
            "calories": 0
        }
    },
    "side_options": {
        1: {
            "name": "Fries",
            "calories": 100
        },
        2: {
            "name": "Potato",
            "calories": 57
        },
        3: {
            "name": "Salad",
            "calories": 70
        },
        4: {
            "name": "No Side",
            "calories": 0
        }
    },
    "drink_options": {
        1: {
            "name": "Soda",
            "calories": 130
        },
        2: {
            "name": "OJ",
            "calories": 160
        },
        3: {
            "name": "Milk",
            "calories": 118
        },
        4: {
            "name": "No Drink",
            "calories": 0
        }
    },
    "dessert_options": {
        1: {
            "name": "Apple Pie",
            "calories": 167
        },
        2: {
            "name": "Sundae",
            "calories": 266
        },
        3: {
            "name": "Fruit Cup",
            "calories": 75
        },
        4: {
            "name": "No Dessert",
            "calories": 0
        }
    }
}

food_cal = menu["burger_options"][burger]["calories"]
side_cal = menu["side_options"][side]["calories"]
drink_cal = menu["drink_options"][drink]["calories"]
dessert_cal = menu["dessert_options"][dessert]["calories"]

total_cals = food_cal + side_cal + drink_cal + dessert_cal

print(f"Your total Calorie count is {total_cals}.")
