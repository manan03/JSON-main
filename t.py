import streamlit as st

def remove_code_block():
    st.session_state.show_code_block = False

def main():
    st.title("Code Block Example")
    
    if "show_code_block" not in st.session_state:
        st.session_state.show_code_block = True

    if st.session_state.show_code_block:
        st.code("""
            # Your code here
        """)

    if st.button("Remove Code Block"):
        remove_code_block()

if __name__ == "__main__":
    main()
