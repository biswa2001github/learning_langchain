from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct"
)

model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You are a helpful AI assistant"),
    HumanMessage(content="Tell me about LSTM Model in 2 lines")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)