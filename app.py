import streamlit as st
import time
# Title of the app
st.title("Streamlit Components Demo")

# Display text
st.write("Hello, let's learn how to build a Streamlit app together!")

# Text input
text_input = st.text_input("Enter Your text here: ")

# Button
if st.button("Click Me"):
    st.write('Button clicked!')

# Sidebar
with st.sidebar:
    st.title("Sidebar")

    # Selectbox
    st.write("Select an option:")
    options = ["Option 1", "Option 2", "Option 3"]
    selected_option = st.selectbox("Selectbox", options)
    st.write(f"Selected option: {selected_option}")

    # Checkboxes
    st.write("Check the boxes:")
    checkbox1 = st.checkbox("Checkbox 1")
    checkbox2 = st.checkbox("Checkbox 2")
    st.write(f"Checkbox 1: {checkbox1}, Checkbox 2: {checkbox2}")

# Form handling
st.write("Form Handling:")
with st.form("my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    color = st.selectbox("Favorite Color", ["Red", "Green", "Blue"])
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Favorite Color: {color}")

# Data display
st.write("Data Display:")
import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)
st.table(df)

# Interactive widgets
st.write("Interactive Widgets:")
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"Age: {age}")

number = st.number_input("Enter a number", min_value=0, max_value=100, value=50)
st.write(f"Number: {number}")

# Visualization
st.write("Visualization:")
chart_data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 4, 9, 16, 25]
})
st.line_chart(chart_data)

# File handling
st.write("File Handling:")
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'txt'])
if uploaded_file:
    st.write("File details:")
    st.write(uploaded_file.name)
    st.write(uploaded_file.type)
    st.write(uploaded_file.size)

# Progress bar
st.write("Progress Bar:")
with st.spinner("Processing..."):
    for i in range(100):
        progress = st.progress(i)
        time.sleep(0.1)

# Columns
st.write("Columns:")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
with col3:
    st.write("Column 3")

# Metrics
st.write("Metrics:")
col1, col2 = st.columns(2)
with col1:
    st.metric("Temperature", "22°C", "1.5°C")
with col2:
    st.metric("Humidity", "45%", "-2%")

# Code block
st.write("Code Block:")
with st.echo():
    st.write("This code is displayed as a code block")
