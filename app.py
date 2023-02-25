import openai
import os
from dotenv import load_dotenv
load_dotenv()

def askGPT(text):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        askGPT(myQn)
        print('\n')

main()