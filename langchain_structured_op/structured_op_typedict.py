from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id=''
)