import streamlit as st
st.title("my 1st project")
name = st.text_input("Whats yo name lil boy")
if name :
  st.write(f"hello {name}")
