import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="NEON_CALC", page_icon="⚡", layout="centered")

# 2. Futuristic Theme & Mobile Responsiveness Fixes
st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background-color: #0d0e12;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Wrap the calculator in a centered, bounded container */
    [data-testid="stMainBlockContainer"] {
        max-width: 450px !important;
        padding: 2rem 1rem !important;
        margin: 0 auto !important;
    }
    
    /* FORCE st.columns to stay horizontal on mobile devices instead of stacking vertically */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
    }
    
    /* Make sure every column inside a row shares the space correctly on small screens */
    [data-testid="stHorizontalBlock"] > div {
        min-width: 0 !important;
        flex: 1 1 0% !important;
    }

    /* Adjust sizing for the uneven bottom row (0, ., =) */
    [data-testid="stHorizontalBlock"]:last-of-type > div:last-child {
        flex: 2 1 0% !important;
    }
    
    /* Title styling */
    .title-text {
        text-align: center;
        color: #00ffcc;
        text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
        letter-spacing: 2px;
        margin-bottom: 20px;
        font-size: 1.5rem;
    }

    /* Calculator display box */
    .display-box {
        background-color: #1a1c23;
        border: 2px solid #ff007f;
        box-shadow: 0 0 15px #ff007f;
        border-radius: 10px;
        padding: 15px;
        text-align: right;
        font-size: 2.2rem;
        color: #00ffcc;
        text-shadow: 0 0 5px #00ffcc;
        margin-bottom: 15px;
        word-wrap: break-word;
        overflow-x: auto;
    }

    /* Button styling override */
    div.stButton > button {
        background-color: #1a1c23 !important;
        color: #00ffcc !important;
        border: 1px solid #00ffcc !important;
        box-shadow: 0 0 5px #00ffcc !important;
        transition: all 0.2s ease;
        width: 100% !important;
        font-weight: bold;
        font-size: 1.4rem !important;
        padding: 12px 0px !important;
        border-radius: 6px !important;
    }
    
    div.stButton > button:hover, div.stButton > button:active {
        background-color: #00ffcc !important;
        color: #0d0e12 !important;
        box-shadow: 0 0 15px #00ffcc !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. App Title
st.markdown("<h1 class='title-text'>// SYSTEM_CALC_v1.1</h1>", unsafe_allow_html=True)

# 4. Initialize Session State for Memory
if "expression" not in st.session_state:
    st.session_state.expression = ""

# 5. Live Display
st.markdown(f"<div class='display-box'>{st.session_state.expression if st.session_state.expression else '0'}</div>", unsafe_allow_html=True)

# 6. Grid Layout for Buttons (using use_container_width=True to fill mobile space)
# Row 1
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("C", use_container_width=True): 
        st.session_state.expression = ""
        st.rerun()
with col2:
    if st.button("(", use_container_width=True): 
        st.session_state.expression += "("
        st.rerun()
with col3:
    if st.button(")", use_container_width=True): 
        st.session_state.expression += ")"
        st.rerun()
with col4:
    if st.button("/", use_container_width=True): 
        st.session_state.expression += "/"
        st.rerun()

# Row 2
col5, col6, col7, col8 = st.columns(4)
with col5:
    if st.button("7", use_container_width=True): 
        st.session_state.expression += "7"
        st.rerun()
with col6:
    if st.button("8", use_container_width=True): 
        st.session_state.expression += "8"
        st.rerun()
with col7:
    if st.button("9", use_container_width=True): 
        st.session_state.expression += "9"
        st.rerun()
with col8:
    if st.button("*", use_container_width=True): 
        st.session_state.expression += "*"
        st.rerun()

# Row 3
col9, col10, col11, col12 = st.columns(4)
with col9:
    if st.button("4", use_container_width=True): 
        st.session_state.expression += "4"
        st.rerun()
with col10:
    if st.button("5", use_container_width=True): 
        st.session_state.expression += "5"
        st.rerun()
with col11:
    if st.button("6", use_container_width=True): 
        st.session_state.expression += "6"
        st.rerun()
with col12:
    if st.button("-", use_container_width=True): 
        st.session_state.expression += "-"
        st.rerun()

# Row 4
col13, col14, col15, col16 = st.columns(4)
with col13:
    if st.button("1", use_container_width=True): 
        st.session_state.expression += "1"
        st.rerun()
with col14:
    if st.button("2", use_container_width=True): 
        st.session_state.expression += "2"
        st.rerun()
with col15:
    if st.button("3", use_container_width=True): 
        st.session_state.expression += "3"
        st.rerun()
with col16:
    if st.button("+", use_container_width=True): 
        st.session_state.expression += "+"
        st.rerun()

# Row 5
col17, col18, col19 = st.columns([1, 1, 2])
with col17:
    if st.button("0", use_container_width=True): 
        st.session_state.expression += "0"
        st.rerun()
with col18:
    if st.button(".", use_container_width=True): 
        st.session_state.expression += "."
        st.rerun()
with col19:
    if st.button("=", use_container_width=True):
        try:
            result = eval(st.session_state.expression)
            st.session_state.expression = str(result)
        except Exception:
            st.session_state.expression = "ERROR"
        st.rerun()
