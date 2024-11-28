import streamlit as st
import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

if 'html' not in st.session_state:
  st.session_state.html = ''
  st.session_state.header = ""

st.title("Streamlit on Replit")

with st.form(key="req_html"):
  url = st.text_input(label="Url:")
  h = st.text_input(label="Header:") 
  if h != "":
    header = {"User-Agent": h}
  submit = st.form_submit_button(label="Submit")
  if submit:
    st.session_state.html = requests.get(url, headers=header).text
    st.session_state.header = header

st.write(st.session_state.header)
st.code(st.session_state.html)
