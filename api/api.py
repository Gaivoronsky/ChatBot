import streamlit as st
from db.db import ClassDB


with st.form("my_form"):
    token = st.text_input('Input token', '')

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Token: ", token)

if token and len(token) == 5:
    db = ClassDB()
    db.add_token(token)
    st.write("Nice!")
else:
    st.write('Чёт не то(')
