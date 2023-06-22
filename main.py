import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
from U2_main import usecase_2
from running_stack import get_stack_list
from fileMap_CF import Map
from U1_main import usecase_1
from Transformation_model import transform_model
import streamlit as st
import subprocess
from fontawesome import icons

st.set_page_config(layout="wide")  # Set the page layout to wide
st.title(':blue[LANDING ZONE TRANSFORMATION]')
def remove_code_block():
    st.session_state.show_code_block = False
def stack():
    get_stack_list()
def update_makefile():
    makefile_content = f""".PHONY: download-and-run
   
download-and-run:
\taws cloudformation get-template --stack-name {stack_name} --output json > temp1.json
"""
    # Write the updated Makefile
    with open("makefile", "w") as f:
        f.write(makefile_content)

    # Display a confirmation message
    st.write("Makefile updated with stack name: {}".format(stack_name))
    subprocess.call(['make', '-f', './makefile'])
    usecase_1()
def extract():
    json_string3  = usecase_2(input_json_string,selected_items)
    json_data3 = json.loads(json_string3)
    with st.expander("See code"):
        st.code(json.dumps(json_data3, indent=4), language='json') 

st.markdown(
    """
    <style>
    .stButton>button {
        width: 12%;
        box-sizing: border-box;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#################### USE CASE-1 ########################

st.subheader('_Use Case 1: Transformation Model_')
input_json_string2 = st.text_area("", value="", height=100, help="Provide your JSON input here which you want to transform into OCI landing zone", key="json_input1", placeholder="Enter JSON here...")

st.session_state.show_codeblock = True
if st.button("TRANSFORM",key=1):
    transform_model(input_json_string2)    
st.divider() 

#################### USE CASE-2 ########################

st.subheader('_Use Case 2: Get Stack List and Transform_')
st.write("\n")
if st.button("GET STACK LIST"):
    stack()

stack_name = st.text_area("" ,value="", height=100, help="Provide your stack name here which you want to transform into OCI landing zone", key="json_input2", placeholder="Enter Stack name here...")
if st.button("TRANSFORM",key=2):
    update_makefile()
st.divider()       

#################### USE CASE-3 #########################
st.subheader('_Use Case 3: Give Resource names and Extract_')
input_json_string = st.text_area('', value="", height=100, help="Provide your JSON input", key="json_input3", placeholder="Enter JSON here...")
res_list_name = st.text_input("LIST RESOURCES",placeholder="List of resources",help="Provide list of resources you want to transform into OCI")
selected_items = [item.strip() for item in res_list_name.split(',')]

if st.button("TRANSFORM",key=3):
    extract()


