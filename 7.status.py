import streamlit as st
import time

st.title("Status")

# Progress 바
st.progress(value=50)

#특수 효과.
st.balloons()

# 메시지 출력 
# 주의 : icon은 1개씩만 사용"🚨"
st.error('This is an error', icon = "🚨")
st.warning('This is a warning', icon="⚠️")
st.info('This is a purely informational message', icon="ℹ️")
st.success('This is a success message!', icon="✅")
#https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/


# Spinner
with st.spinner(text = '실행중...'):
    time.sleep(3.0)
    st.success( '종료!', icon = '😊')
