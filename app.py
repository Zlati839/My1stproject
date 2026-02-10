import streamlit as st
st.title("Math test")
color = st.text_input("Whats 2+2 ")
if color == 4:
  st.success(f"Correct!!")
 else:
    st.warning(f"Wrong")
Subject = st.text_input("Whats 10/2 ")
if Subject:
  if Subject == 5:
    st.success(f"Correct!!")
  else:
    st.warning(f"Wrong")

Hobby = st.text_input("Whats 4(100*2) ?")
if Hobby:
  if Hobby == 800:
    st.success(f"Correct!!")
  else:
    st.warning(f"Wrong")

Age = st.text_input("Whats 10000000000 - 1  ?")
if Age:
   if Age == 9999999999:
     st.success(f"Correct!!")
   else:
     st.warning(f"Wrong")
