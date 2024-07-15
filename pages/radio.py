import streamlit as st

genre = st.radio(
    "다음 중 C 명령어가 아닌 것은?",
    ["printf();", "int main()", "!DOCTYPEHTML", "if()", "for()"],
    index=None,
)

if st.button("제출"):
    st.write("제출되었습니다.")