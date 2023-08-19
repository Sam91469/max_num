import streamlit as st
st.write('# streamlit application for finding the largest among the 3 given numbers')
st.write('#User Input Parameters')
number1 = st.number_input('Insert a first number')
st.write('The current number is ', number1)
number2 = st.number_input('Insert a second number')
st.write('The current number is ', number2)
number3 = st.number_input('Insert a third number')
st.write('The current number is ', number3)
st.write('The max number is:')
st.write(max(number1,number2,number3))
!streamlit run app.py & npx localtunnel --port 8501
