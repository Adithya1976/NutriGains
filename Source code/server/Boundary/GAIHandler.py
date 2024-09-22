import google.generativeai as genai
import os
"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
class GAIHandler:
    def __init__(self, history):
        self.api_key=GEMINI_API_KEY
        genai.configure(api_key=self.api_key)

        # Set up the model
        generation_config = {
            "temperature": 0.5,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)

   
        self.chat = model.start_chat(history=history)
    def getResponse(self, msg):
        response = self.chat.send_message(msg)
        return response.text
