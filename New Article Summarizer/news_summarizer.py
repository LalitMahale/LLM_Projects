import streamlit as st
import os
from dotenv import load_dotenv
from newspaper import Article
import requests
from langchain.schema import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()




API_KEY = os.getenv("GOOGLE_GEMINI_API")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

article_url = "https://www.artificialintelligence-news.com/2022/01/25/meta-claims-new-ai-supercomputer-will-set-records/"

session = requests.Session()

template = '''You are good in article summarization.
Here is the article to summarize.
----------------
Title:{article_title}

{article_text}
----------------

write a summary of the given article.
'''


chat = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=API_KEY, temperature=0)



st.header("News Summarizer")

def get_article(article_url):
    try:
        response = session.get(article_url, headers = headers , timeout = 10)

        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()

            return article.title, article.text
        else:
            # st.error('This is an error', icon="🚨")

            st.error(f"failed to fetch article at {article_url}")
    except Exception as e:
        st.error(f"Error occured at : {e}")

url = st.text_input("Article URL")
button = st.button("Submit")
if button:
    title, text = get_article(url)
    # col1 , col2 = st.columns(2)
    # with col1:

    # with col2:
    prompt = template.format(article_title=title, article_text=text)
    messages = [HumanMessage(content=prompt)]
    st.subheader("\t\tSummary : ")
    # st.subheader("Title: ",title)
    st.write(chat(messages=messages).content)
    checkbox = st.checkbox("Read Full article")
    if checkbox:
        st.subheader(f"Title: {title}")
        st.write(f"{text}")