import streamlit as st


title = st.text_input("Save")
if st.button("save"):
    st.session_state.title = "title"