import streamlit as st
from logic import add

st.title("Hello App")

st.subheader("Add two numbers")

a = st.number_input("First number", value=0)
b = st.number_input("Second number", value=0)

if st.button("Add"):
    st.write(f"{a} + {b} = {add(a, b)}")