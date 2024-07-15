import streamlit as st


title = st.text_input("학번,이름")
if st.button("save"):
    st.session_state.title = "title"