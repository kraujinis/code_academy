# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate
    
    
    
# class Person:
#     def __init__(self, name: str, hate_food: list, like_food: list) -> None:
#         self.name = name
#         self.hate_food = hate_food
#         self.like_food = like_food
        
#     def foods_they_hate(self) -> None:
#         hate_food_list = []
#         for n in self.hate_food:
#             hate_food_list.append(n)
#         print(f'{self.name} hate this food: {hate_food_list}')

#     def foods_they_like(self) -> None:
#         like_food_list = []
#         for n in self.like_food:
#             like_food_list.append(n)
#         print(f'{self.name} like this food: {like_food_list}')
    
        
        
# p = Person('John', ['meat', 'carrot'], ['juise', 'apple'])

# p.foods_they_hate()
# p.foods_they_like()
from typing import List


class Person:
    def __init__(self, name: str, hate_food: List[str], like_food: List[str]): 
      self.name = name
      self.hate_food = hate_food
      self.like_food = like_food
      
    def food(self, food: str) -> None:
        if food in self.hate_food:
            print(f'{self.name} hate this food: {food}')
        if food in self.like_food:
            print(f'{self.name} like this food: {food}')
            
            
person = Person('John', hate_food=['meat', 'bananas'], like_food=['juice', 'apple'])
person.food('meat')
person.food('apple')


