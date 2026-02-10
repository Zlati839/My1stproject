import streamlit as st
st.title("my 1st project")
name = st.text_input("Whats your name ")
if name :
  st.write(f"hello {name}")
  
color = st.text_input("Whats your favorite color ")
if color :
  st.write(f"{color} is a nice color")

Subject = st.text_input("Whats your favorite subject ")
if Subject :
  st.write(f"{Subject} , intresting")
