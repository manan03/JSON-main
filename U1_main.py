import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
from fileMap_CF import Map
import streamlit as st
import os
def remove_code_block():
    st.session_state.show_code_block = False
def u1():
    # Read the JSON file
    with open('temp1.json') as file:
        json_data2 = json.load(file)

    # Convert JSON to string
    json_string2 = json.dumps(json_data2)

    version1 = "No reference file present"
    json_string1 = ""
    if(json_string2.find('$schema')==-1):
        for key in Map.keys():
            if key in json_string2:
                with open(Map[key]) as file:
                    json_data1 = json.load(file)
                    if "TemplateBody" in json_data1:
                        version1 = json_data1["TemplateBody"]["AWSTemplateFormatVersion"]
                    else:
                        version1 = json_data1["AWSTemplateFormatVersion"]
                    json_string1 = json.dumps(json_data1)
                break
                
        json_data2 = json.loads(json_string2)
        if "TemplateBody" in json_data2:
            version2 = json_data2["TemplateBody"]["AWSTemplateFormatVersion"]
        else:
            version2 = json_data2["AWSTemplateFormatVersion"]

        print(version2)
        print(version1)

        if(version1 == version2 or version2=="2010-09-09"):
            print("Up to date")
            json_string2 = transformit(json_string2)
            json_data3 = json.loads(json_string2)

            # Display the JSON string in a textarea
            if "show_code_block" not in st.session_state:
                st.session_state.show_code_block = True
            if st.button("Remove Code Block"):
                remove_code_block()
            if st.session_state.show_code_block:
                st.code(json.dumps(json_data3, indent=4), language='json')
        else:
            print("New")
            dict1[version1]=version2

            # Write the JSON object to a file
            with open('temp1.json', 'w') as file:
                json.dump(json_data2, file, indent=4)

            with open("find.py") as f:
                exec(f.read())
            json_string2 = transformit(json_string2)
            json_data3 = json.loads(json_string2)
            if "show_code_block" not in st.session_state:
                st.session_state.show_code_block = True
            if st.button("Remove Code Block"):
                remove_code_block()
            if st.session_state.show_code_block:
                st.code(json.dumps(json_data3, indent=4), language='json')
