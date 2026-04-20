import streamlit as st

st.set_page_config(page_title="Advanced Calculator", page_icon="🧮")

st.title("🧮 Advanced Calculator")

# Inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose operation",
    ["Add", "Subtract", "Multiply", "Divide", "Percentage", "Power", "Remainder"]
)

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    elif operation == "Percentage":
        result = (num1 / num2) * 100 if num2 != 0 else "Invalid"
    elif operation == "Power":
        result = num1 ** num2
    elif operation == "Remainder":
        result = num1 % num2

    st.success(f"Result: {result}")