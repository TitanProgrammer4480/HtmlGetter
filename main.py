import streamlit as st
import requests

if 'html' not in st.session_state:
  st.session_state.html = ''

st.title("Streamlit on Replit")

with st.form(key="req_html"):
  url = st.text_input(label="Url:")
  submit = st.form_submit_button(label="Submit")
  if submit:
    st.session_state.html = requests.get(url).text
st.code(st.session_state.html)