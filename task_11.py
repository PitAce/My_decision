class Dessert:
  
    def __init__(self, name = None, calories = 0):
        self.__name = name
        self.__calories = calories
      
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def calories(self):
        return self.__calories
        
    @calories.setter
    def calories(self, calories):
        self.__calories = calories
       
    def is_healthy(self):
        if (((type(self.__calories) == int) or (isinstance(self.__calories, float))) and self.__calories < 200):
            return True
        return False
        
    def is_delicious(self):
        return True
