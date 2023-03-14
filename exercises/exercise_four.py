# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients,
#     add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.

from typing import Dict, Optional


class Smoothie:
    multiplicator = 1.5

    def __init__(self, **ingredients) -> None:
        self.ingredients = ingredients

    def get_cost(self) -> float:
        cost_of_all_ingredients = sum(self.ingredients.values())
        print(f"Cost of all ingredients: {cost_of_all_ingredients}")
        return cost_of_all_ingredients

    def get_price(self) -> float:
        price_of_all_ingredients = round(self.get_cost() * self.multiplicator, 2)
        print(f"Price of all ingredients: {price_of_all_ingredients}")
        return price_of_all_ingredients

    def get_name(self) -> list:
        names_of_all_ingredients = []
        for keys in self.ingredients.keys():
            names_of_all_ingredients.append(keys)
        sorted_ingredients = sorted(names_of_all_ingredients)
        list_set = set(names_of_all_ingredients)
        if len(list_set) == len(names_of_all_ingredients):
            print(
                f'You smothie has ingredients: {", ".join(sorted_ingredients)}.Fusion.'
            )
        else:
            print(
                f'You smothie has ingredients: {", ".join(sorted_ingredients)}.Smothie.'
            )

        return sorted_ingredients


class Ingredients:
    def __init__(self) -> None:
        pass

    def ingredients_list(self):
        ingredients_list = {"apple": 1.12, "strawberry": 0.98, "water": 1.45}


ingredients = Smoothie(vodka=15, juice=1.58, water=0.84, apple=4.5)
ingredients.get_cost()
ingredients.get_price()
ingredients.get_name()

x = 5
y = x**2 + 5
z = (x + y) * (x - y)
