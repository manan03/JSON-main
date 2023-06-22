import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
from running_stack import get_stack_list
from fileMap_CF import Map
import U1_main
import streamlit as st
import os
import subprocess
 

def transform_model(input_json_string2):
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

            if "show_code_block" not in st.session_state:
                st.session_state.show_code_block = True
            st.download_button('_Download as file_', output_json_string2)
            if st.session_state.show_code_block:
                with st.expander("See explanation"):
                    st.code(json.dumps(json_data3, indent=4), language='json')

            
        else:
            print("New")
            dict1[version1]=version2

            with open("find.py") as f:
                exec(f.read())
            output_json_string2 = transformit(input_json_string2)
            json_data3 = json.loads(output_json_string2)
            
            if "show_code_block" not in st.session_state:
                st.session_state.show_code_block = True
            st.download_button('Download some text', output_json_string2)
            if st.session_state.show_code_block:
                st.code(json.dumps(json_data3, indent=4), language='json')
            
    else:
        output_json_string2 = transformit2(input_json_string2)
        json_data3 = json.loads(output_json_string2)
        
        if "show_code_block" not in st.session_state:
            st.session_state.show_code_block = True
        if st.session_state.show_code_block:
            st.code(json.dumps(json_data3, indent=4), language='json')