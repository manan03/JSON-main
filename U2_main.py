import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
import sys
# Read the JSON file
with open('temp1.json') as file:
    json_data2 = json.load(file)

if "TemplateBody" in json_data2:
    res_data = json_data2["TemplateBody"]["Resources"]["InstanceSecurityGroup"]
    output_dict = {
        "InstanceSecurityGroup": res_data
    }
    res_string =json.dumps(output_dict, indent=4)
    print(res_string)
    json_string2 = transformit(res_string)
else:
    res_data = json_data2["Resources"]["InstanceSecurityGroup"]
    output_dict = {
        "InstanceSecurityGroup": res_data
    }
    res_string =json.dumps(output_dict, indent=4)
    print(res_string)
    json_string2 = transformit(res_string)   
