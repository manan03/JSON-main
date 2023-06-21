import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
from U2_main import U2
from running_stack import get_stack_list
from fileMap_CF import Map
from U1_main import u1
import U1_main
import streamlit as st
import os
import subprocess



st.title("LANDING ZONE TRANSFORMATION")
input_json_string2 = st.text_area("TRANSFORMATION MODEL WITH USE CASE-1 (ENTER JSON STRING)")

def transform_model():
    version1 = "No reference file present"
    if(input_json_string2.find('$schema')==-1):
        for key in Map.keys():
            if key in input_json_string2:
                with open(Map[key]) as file:
                    ref_json_data1 = json.load(file)
                    if "TemplateBody" in ref_json_data1:
                        version1 = ref_json_data1["TemplateBody"]["AWSTemplateFormatVersion"]
                    else:
                        version1 = ref_json_data1["AWSTemplateFormatVersion"]
                break
    
        json_data2 = json.loads(input_json_string2)
        if "TemplateBody" in json_data2:
            version2 = json_data2["TemplateBody"]["AWSTemplateFormatVersion"]
        else:
            version2 = json_data2["AWSTemplateFormatVersion"]

        print(version2)
        print(version1)

        if(version1 == version2 or version2=="2010-09-09"):
            print("Up to date")
            output_json_string2 = transformit(input_json_string2)
            json_data3 = json.loads(output_json_string2)

            # Display the JSON string in a textarea
            st.code(json.dumps(json_data3, indent=4), language='json')
        else:
            print("New")
            dict1[version1]=version2

            with open("find.py") as f:
                exec(f.read())
            output_json_string2 = transformit(input_json_string2)
            json_data3 = json.loads(output_json_string2)

            st.code(json.dumps(json_data3, indent=4), language='json')
            
    else:
        output_json_string2 = transformit2(input_json_string2)
        json_data3 = json.loads(output_json_string2)

        # Display the JSON string in a textarea
        st.code(json.dumps(json_data3, indent=4), language='json')
        
# Button to trigger the transformation
if st.button("TRANSFORM"):
    transform_model()

#################### USE CASE-2 ########################
def stack():
    get_stack_list()
if st.button("Get Stack List"):
    stack()

stack_name = st.text_area("USE CASE-2 (ENTER STACK NAME)")
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
    u1()
    
if st.button("GENERATE"):
    update_makefile()
        
#################### USE CASE-3 #########################

input_json_string = st.text_area("USE CASE-3 (ENTER JSON STRING)")
res_list_name = st.text_input("LIST RESOURCES")
selected_items = [item.strip() for item in res_list_name.split(',')]

def extract():
    json_string3  = U2(input_json_string,selected_items)
    json_data3 = json.loads(json_string3)
    st.code(json.dumps(json_data3, indent=4), language='json') 
    
if st.button("Extract"):
    extract()

