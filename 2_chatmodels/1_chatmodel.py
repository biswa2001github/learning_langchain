from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

result = llm.invoke('Suggest me 5 top engineering branches.')

print(result.text)

