import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# Model definition
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
)

model = ChatHuggingFace(llm=llm)

# App layout
st.header('Research Tool')

paper_ip = st.selectbox("Select the paper for summarization", ["Attention is All you need", "Speculative Decoding by Levianthan", "GPT-3: Language models are Few-Shot Learners"])
style_ip = st.selectbox("Select style for summarization", ["Beginner friendly", "Code-oriented", "Mathematical oriented"])
length_ip = st.selectbox("Select explanation style", ["Short ,1-2 paragraphs", "Medium, 4-5 paragraphs", "Long, 6+ paragraphs"])

# filling the placeholders
template = load_prompt('prompts/template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper':paper_ip,
        'style':style_ip,
        'length':length_ip
    })
    st.text(result.content)

