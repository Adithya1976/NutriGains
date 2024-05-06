Dependencies to Install:

1) Flask
2) Flask-cors
3) SQLAlchemy
4) google-generativeai

Configurations:

* Database URL:
  * File: /Boundary/DatabaseCRUDOperator.py
  * function: __init__
  * variable: self.db_url
* Gemini API Key:
  * File: /Boundary/GAIHandler.py
  * function: __init__
  * variable: self.api_key
* Spoonacular API Key:
  * File: /Boundary/NutritionAPIHandler.py
  * class: NutritionAPIHandler
  * variable: APIKey


To run the backend:

* run the server.py file
