import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
import streamlit as st

def usecase_2(json_string2,stack_list):
    json_data2 = json.loads(json_string2)
    final_string=""
    if "TemplateBody" in json_data2:
        for s in stack_list :
            print(s)
            res_data = json_data2["TemplateBody"]["Resources"][s]
            output_dict = {
                s: res_data
            }
            res_string =json.dumps(output_dict, indent=4)
            res_string = res_string[1:-1]+","
            final_string=final_string+res_string
        final_string = final_string[:-1]
        final_string= "{"+final_string+"}"
    else:
        for s in stack_list :
            print(s)
            res_data = json_data2["Resources"][s]
            output_dict = {
                s: res_data
            }
            res_string =json.dumps(output_dict, indent=4)
            res_string = res_string[1:-1]+","
            final_string=final_string+res_string
        final_string = final_string[:-1]
        final_string= "{"+final_string+"}"

    json_string2 = transformit(final_string)   
    return json_string2

def all_usecase_2(json_string2):
    json_data2 = json.loads(json_string2)
    final_string=""
    if "TemplateBody" in json_data2:
        
        res_data = json_data2["TemplateBody"]["Resources"]

        res_string =json.dumps(res_data, indent=4)

        final_string= res_string
    else:
        res_data = json_data2["Resources"]

        res_string =json.dumps(res_data, indent=4)

        final_string= res_string

    json_string2 = transformit(final_string)
    st.download_button('_Download as file_',json_string2)
 
    return json_string2