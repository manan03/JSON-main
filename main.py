import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
from fileMap_CF import Map
import U1_main
import streamlit as st
# import pyperclip
import os
import subprocess

json_string=""

# Streamlit UI
st.title("Landing Zone Transformation")

# Textarea to enter JSON string
json_string2 = st.text_area("Enter JSON string")

# Button to trigger the transformation
if st.button("Transform"):
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

            # Display the textarea and copy button
            with st.container():
                text_area = st.text_area("JSON String", value=json_string2, height=150)
                copy_button = st.button("Copy")

            if copy_button:
                st.experimental_set_query_params(text_area)
            # Print the JSON string
            st.code(json.dumps(json_data3, indent=4), language='json')
            
    else:
        json_string2 = transformit2(json_string2)
        json_data3 = json.loads(json_string2)

        # Display the JSON string in a textarea
        st.code(json.dumps(json_data3, indent=4), language='json') 

stack_name = st.text_area("Enter stack name")
def update_makefile():
    makefile_content = f""".PHONY: download-and-run

download-and-run:
\taws cloudformation get-template --stack-name {stack_name} --output json > temp1.json && python U1_main.py
"""
    # Write the updated Makefile
    with open("makefile", "w") as f:
        f.write(makefile_content)

    # Display a confirmation message
    st.write("Makefile updated with stack name: {}".format(stack_name))
    subprocess.call(['make', '-f', './makefile'])
    st.code(json.dumps(U1_main.json_data3, indent=4), language='json') 

if st.button("Update Makefile"):
    update_makefile()
        

