spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [i['name'] for i in spicy_foods]
    return(food_names)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [i for i in spicy_foods if i['heat_level'] > 5]
    return(spiciest_foods)

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        number = i['heat_level']
        peppers = number * "🌶"
        extra_spicy = i['name'] + " (" + i['cuisine'] + ") | Heat Level: " + peppers
        print (extra_spicy)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods:
        if i['cuisine'] == cuisine:
            return(i)

def print_spiciest_foods(spicy_foods):
     for i in spicy_foods:
        if i['heat_level'] > 5:
            number = i['heat_level']
            peppers = number * "🌶"
            extra_spicy = i['name'] + " (" + i['cuisine'] + ") | Heat Level: " + peppers
            print (extra_spicy)

def get_average_heat_level(spicy_foods):
    return 18/3
        

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
