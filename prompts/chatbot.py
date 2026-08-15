from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct"
)

model = ChatHuggingFace(llm=llm)
chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user_ip = input("You: ")
    chat_history.append(HumanMessage(content=user_ip))
    if user_ip == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(f"Chat history: {chat_history}")