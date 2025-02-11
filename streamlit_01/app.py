import streamlit as st 
import pandas as pd
import numpy as np

# Title
st.title('My first app')
# Simple text
st.write('Here is our first attempt at using data to create a table:')
df = pd.DataFrame({
    'first_col': [1,2,3,4],
    'second_col': [10,20,30,40]
})

st.write("Dataset:")
st.write(df)

# Line CHart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

name = st.text_input("Enter your name")
age = st.slider("How old are you?", 0, 130, 25)
options = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
if name: 
    st.write(f"Hello {name}")
st.write(f"I'm {age} years old")
st.write(f"You selected {options}")
