import pathlib
import textwrap
import os
import google.generativeai as genai

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


def ask_gemini(req):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(req)
    return response.candidates[0].content.parts[0].text
    


print(handle('What is my name?'))




def handle(event, context):
    
    return {
        "statusCode": 200,
        "body": ask_gemini('What is my name?')
    }
