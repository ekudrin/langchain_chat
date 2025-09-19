
import streamlit as st

st.set_page_config(page_title='Chatbot')

st.title('Chatbot')

with st.sidebar:
    st.header('Settings')
    website_url = st.text_input('Website URL')

