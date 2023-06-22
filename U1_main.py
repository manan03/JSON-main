import json
from Transformation_model import transform_model
import streamlit as st

def remove_code_block():
    st.session_state.show_code_block = False
def usecase_1():
    with open('temp1.json') as file:
        json_data2 = json.load(file)
    input_json_string2 = json.dumps(json_data2)
    transform_model(input_json_string2)