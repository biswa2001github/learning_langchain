from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# This will load environment variables
load_dotenv()

# Initilaise LLM
llm = GoogleGenerativeAI(model="gemini-3.5-flash")

result = llm.invoke("What is the capital of India?")

print(result)
