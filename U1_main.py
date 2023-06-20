import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
from fileMap_CF import Map
# import streamlit as st
# import pyperclip
import os

json_string=""

# Read the JSON file
with open('temp1.json') as file:
    json_data2 = json.load(file)

# Convert JSON to string
json_string2 = json.dumps(json_data2)

# Streamlit U
#  st.title("JSON Transformation Tool")

# Textarea to enter JSON string
# json_string2 = st.text_area("Enter JSON string")

# Button to trigger the transformation
# if st.button("Transform"):
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
        # st.code(json.dumps(json_data3, indent=4), language='json')
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

        # st.markdown(
        #     """
        #     <style>
        #     .copyable-textarea-container {
        #         position: relative;
        #     }
        #     .copyable-textarea {
        #         width: 100%;
        #         height: auto;
        #         min-height: 150px;
        #         resize: vertical;
        #         padding: 10px;
        #         background-color: #f0f0f0;
        #     }
        #     .copy-button {
        #         position: absolute;
        #         top: 5px;
        #         right: 10px;
        #     }
        #     </style>
        #     """,
        #     unsafe_allow_html=True
        # )

        # # Display the textarea and copy button
        # with st.container():
        #     text_area = st.text_area("JSON String", value=json_string2, height=150)
        #     copy_button = st.button("Copy")

        # if copy_button:
        #     st.experimental_set_query_params(text_area)
        # Print the JSON string
        # st.code(json.dumps(json_data3, indent=4), language='json')




















# else:
#     print('This is azure')
#     if(json_string2.find('AutoScalingMultiAZWithNotifications')!= -1):
#         # Read the JSON file
#         with open('AS.json') as file:
#             json_data1 = json.load(file)

#     elif(json_string2.find('ELBWithLockedDownAutoScaledInstances')!= -1):
#         # Read the JSON file
#         with open('ELB.json') as file:
#             json_data1 = json.load(file)
        
#     elif(json_string2.find('EC2InstanceWithSecurityGroupSample')!= -1):
#         # Read the JSON file
#         with open('EC2.json') as file:
#             json_data1 = json.load(file)

#     version2 = json_data2["AWSTemplateFormatVersion"]
#     print(version2)
#     version1 = json_data1["AWSTemplateFormatVersion"]
#     print(version1)

#     if(version1 == version2):
#         print("Up to date")
#         transformit2()
#     else:
#         print("old")
#         dict2[version1]=version2
#         with open("find.py") as f:
#             exec(f.read())
#         transformit2()
