import openai
import config

openai.api_key = config.API_key 

response = openai.ChatCompletion.create(
    model="GPT-4o",
    messages=[{
        "role": "user",
        "content": "¿cúal es el proposito de la vida?"
    }]
)