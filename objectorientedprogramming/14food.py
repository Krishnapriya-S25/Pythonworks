class Cusine:
    cusine_name:str
    def __init__(self,cusine_name):
        self.cusine_name=cusine_name
    def display_cusine_info(self):
        print(self.cusine_name)

class MealType:
    meal_name:str
    def __init__(self,meal_name):
        self.meal_name=meal_name
    def display_meal_info(self):
        print(self.meal_name)

class Dish(Cusine,MealType):
    dish_name:str
    def __init__(self,cusine_name,meal_name,dish_name):
        Cusine.__init__(self,cusine_name)
        MealType.__init__(self,meal_name)
        self.dish_name=dish_name
    def display_dish_info(self):
        print(self.dish_name)

dish_instance=Dish("indian","breakfast","dosa")
dish_instance.display_cusine_info()
dish_instance.display_meal_info()
dish_instance.display_dish_info()



        
    

        

        
    
