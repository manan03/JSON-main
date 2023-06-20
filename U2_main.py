import json
from CF_dictionary import dict1
from Azure_dictionary import dict2
from CF_transform import transformit
from Azure_transform import transformit2
import sys
# Read the JSON file
with open('temp1.json') as file:
    json_data2 = json.load(file)

final_string=""
r = ["WebServerGroup","ApplicationLoadBalancer"]
if "TemplateBody" in json_data2:
    for s in r :
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
    print(final_string)
else:
    for s in r :
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
    print(final_string)
json_string2 = transformit(final_string)   