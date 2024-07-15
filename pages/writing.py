import streamlit as st

st.write("구조체 명령어를 입력하시오.")

user_input = st.text_input(label="정답을 여기에 쓰세요.")

if st.button("제출"):
    if user_input:
        st.write(f"제출되었습니다.")
    else:
        st.write("정답을 다시 제출해주세요.")
