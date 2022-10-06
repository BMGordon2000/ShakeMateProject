from Shake import *
from User import *
from Ingredient import *


#TODO find out exactly what parameter should be used
def get_selected_recipes(ingredients: Ingredients) -> List[Recipes]:
    """
    This method returns a list of of recipes that involve some or all of the elements in the parameter,
    a list of ingredients. 
    param: List of ingredients 
    return: List of recipes
    """