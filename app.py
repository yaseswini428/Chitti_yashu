#give simple streamlit app that can showcase the use of streamlit and the different components of streamlit
import streamlit as st
#from dotenv import load_dotenv
#print helloworld in streamlit
st.write("hello world")
#give me a button that says "click me" and when clicked it will print "button clicked"
if st.button("click me"):
    st.write("button clicked")
#give me a checkbox that says "click me" and when clicked it will print "checkbox clicked"
if st.checkbox("click me"):
    st.write("checkbox clicked")
#give me a radio button that says "click me" and when clicked it will print "radio button clicked"
if st.radio("click me", ["option 1", "option 2", "option 3"]):
    st.write("radio button clicked")