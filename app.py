import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

# --- 3D GREY BUTTON STYLE ---
st.markdown("""
<style>

/* Display */
input {
    font-size: 32px !important;
    text-align: right !important;
    background: linear-gradient(145deg, #2c2f36, #1e2127) !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 15px !important;
}

/* Buttons */
.stButton > button {
    height: 70px;
    width: 100%;
    font-size: 22px;
    font-weight: bold;
    border-radius: 14px;
    border: none;
    margin: 6px;
    
    background: linear-gradient(145deg, #3a3f47, #2b2f36);
    color: white;

    box-shadow: 5px 5px 10px #1c1f26,
                -3px -3px 8px #4a4f57;

    transition: all 0.15s ease-in-out;
}

/* Press effect */
.stButton > button:active {
    box-shadow: inset 3px 3px 6px #1c1f26,
                inset -2px -2px 5px #4a4f57;
    transform: scale(0.97);
}

/* Operators */
.operator button {
    background: linear-gradient(145deg, #ff9f1a, #ff7b00) !important;
}

/* Equal */
.equal button {
    background: linear-gradient(145deg, #34c759, #28a745) !important;
}

/* Clear */
.clear button {
    background: linear-gradient(145deg, #ff3b30, #d32f2f) !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🧮 Calculator")

# --- STATE ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

if "result" not in st.session_state:
    st.session_state.result = ""

# --- FUNCTIONS ---
def add(value):
    st.session_state.expression += str(value)

def clear():
    st.session_state.expression = ""
    st.session_state.result = ""

def calculate():
    try:
        st.session_state.result = str(eval(st.session_state.expression))
    except:
        st.session_state.result = "Error"

# --- INPUT (ENTER KEY ENABLED) ---
expression_input = st.text_input(
    "Enter expression",
    value=st.session_state.expression,
    key="input_box"
)

# Detect Enter press (change in input triggers rerun)
if expression_input != st.session_state.expression:
    st.session_state.expression = expression_input
    try:
        st.session_state.result = str(eval(expression_input))
    except:
        pass

# --- RESULT PANEL ---
st.markdown("### Result")
st.success(st.session_state.result if st.session_state.result else "0")

# --- BUTTON GRID ---
col1, col2, col3, col4 = st.columns(4)

# Row 1
col1.button("7", on_click=add, args=("7",))
col2.button("8", on_click=add, args=("8",))
col3.button("9", on_click=add, args=("9",))
col4.markdown('<div class="operator">', unsafe_allow_html=True)
col4.button("÷", on_click=add, args=("/",))
col4.markdown('</div>', unsafe_allow_html=True)

# Row 2
col1.button("4", on_click=add, args=("4",))
col2.button("5", on_click=add, args=("5",))
col3.button("6", on_click=add, args=("6",))
col4.markdown('<div class="operator">', unsafe_allow_html=True)
col4.button("×", on_click=add, args=("*",))
col4.markdown('</div>', unsafe_allow_html=True)

# Row 3
col1.button("1", on_click=add, args=("1",))
col2.button("2", on_click=add, args=("2",))
col3.button("3", on_click=add, args=("3",))
col4.markdown('<div class="operator">', unsafe_allow_html=True)
col4.button("-", on_click=add, args=("-",))
col4.markdown('</div>', unsafe_allow_html=True)

# Row 4
col1.button("0", on_click=add, args=("0",))
col2.button(".", on_click=add, args=(".",))

col3.markdown('<div class="equal">', unsafe_allow_html=True)
col3.button("=", on_click=calculate)
col3.markdown('</div>', unsafe_allow_html=True)

col4.markdown('<div class="operator">', unsafe_allow_html=True)
col4.button("+", on_click=add, args=("+",))
col4.markdown('</div>', unsafe_allow_html=True)

# Clear
st.markdown('<div class="clear">', unsafe_allow_html=True)
st.button("Clear", on_click=clear)
st.markdown('</div>', unsafe_allow_html=True)
