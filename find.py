import json
import re
from CF_dictionary import dict1
from Azure_dictionary import dict2
from fileMap_CF import Map


def find_words_in_quotes(text):
    pattern = r'"([^"]+)"'
    matches = re.findall(pattern, text)
    word_set = set(matches)
    sorted_words = sorted(word_set, key=lambda word: text.index(f'"{word}"'))
    return sorted_words

# Read the JSON data from temp2.json
with open('temp1.json') as file:
    json_data2 = json.load(file)

# Convert JSON data to a string
json_string2 = json.dumps(json_data2)

version1 = ""
json_string1 = ""
if(json_string2.find('$schema')==-1):

    for key in Map.keys():
        if key in json_string2:
            with open(Map[key]) as file:
                json_data1 = json.load(file)
                version1 = json_data1["AWSTemplateFormatVersion"]
                json_string1 = json.dumps(json_data1)
            break

    # Pass the JSON strings to the UncommonWords function and print the result
    result2 = find_words_in_quotes(json_string2)
    result1 = find_words_in_quotes(json_string1)

    version2 =  json_data2["AWSTemplateFormatVersion"]

    for i in range(len(result2)):
        if(result2[i]==result1[i] or result2[i]== version2):
            continue
        dict1[result2[i]] = dict1[result1[i]]

    with open('CF_dictionary.py', 'w') as file:
        file.write("dict1 = " + json.dumps(dict1, indent=4))

# else:
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

#     # Convert JSON data to a string
#     json_string1 = json.dumps(json_data1)


#     # Pass the JSON strings to the UncommonWords function and print the result
#     result2 = find_words_in_quotes(json_string2)
#     result1 = find_words_in_quotes(json_string1)

#     # print(result2)
#     # print(result1)

#     version1 = json_data1["AWSTemplateFormatVersion"]
#     version2 =  json_data2["AWSTemplateFormatVersion"]

#     for i in range(len(result2)):
#         if(result2[i]==result1[i] or result2[i]== version2):
#             continue
#         dict2[result2[i]] = dict2[result1[i]]

#     with open('Azure_dictionary.py', 'w') as file:
#         file.write("dict1 = " + json.dumps(dict1, indent=4))


# print(dict1)