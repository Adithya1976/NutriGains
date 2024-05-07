import sys
import os
import json
from datetime import datetime

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
sys.path.append(Boundary_dir)
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Entity_dir)

from ConvaAIHandler import ConvaAIHandler
from MealBrowser import MealBrowser
class ConvaChatbot:
    def __init__(self, history):
        self.history = history
    def retrieveMeals(self, filters):
        meals =  MealBrowser.searchResults(filters, 5)
        return meals
    def generate(self, message):
        MealResponse = None
        result = json.loads(ConvaAIHandler.generate(message, False))
        print(result)
        TextResponse = result["message"]
        if result["tool_name"] == "extract_filters":
            MealResponse = self.retrieveMeals(result["parameters"])
        responseDict = {}
        if MealResponse != None:
            MealResponseJson = [meal.jsonify() for meal in MealResponse]
        else:
            MealResponseJson = []
        responseDict["TextResponse"] = TextResponse
        responseDict["MealResponse"] = MealResponseJson
        responseDict["hiddenTextResponse"] = result["parameters"] if MealResponseJson else None
        return responseDict
