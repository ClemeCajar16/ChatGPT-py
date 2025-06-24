import openai
import os 
from dotenv import load_dotenv

load_dotenv() 

openai.api_key = os.getenv("API_key")
 
response = openai.ChatCompletion.create(
    model="GPT-4o",
    messages=[{
        "role": "user",
        "content": "¿cúal es el proposito de la vida?"
    }]
)

