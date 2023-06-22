import streamlit as st

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_session_state():
    if 'session' not in st.session_state:
        st.session_state.session = SessionState(code_block_expanded=True)
    return st.session_state.session

def toggle_code_block():
    session_state = get_session_state()
    session_state.code_block_expanded = not session_state.code_block_expanded

def main():
    st.title("Code Block Example")

    session_state = get_session_state()
    toggle_code_block()

    code_block_expanded = st.sidebar.checkbox("Toggle Code Block", session_state.code_block_expanded)
    if code_block_expanded != session_state.code_block_expanded:
        toggle_code_block()

    if session_state.code_block_expanded:
        st.code("""
            # Your code here
        """)

if __name__ == "__main__":
    main()
