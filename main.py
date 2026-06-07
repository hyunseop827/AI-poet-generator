import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


def generate_poem(subject: str) -> str:
    chat_model = ChatOpenAI()
    result = chat_model.invoke(f"{subject}에 대한 시를 써주겠어요?")
    return result.content


st.set_page_config(page_title="AI Poet Generator")
st.title("인공지능 시인 powered by OpenAI")
subject = st.text_input("시의 주제를 입력해주세요")
st.write("입력된 시의 주제 : " + subject)

has_api_key = bool(os.getenv("OPENAI_API_KEY"))

if not has_api_key:
    st.warning("OPENAI_API_KEY 환경변수를 설정해주세요.")

if st.button("시 작성하기", disabled=not subject.strip() or not has_api_key):
    with st.spinner("작성 중..."):
        poem = generate_poem(subject.strip())
        st.write(poem)

