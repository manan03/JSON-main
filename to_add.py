import json
from CF_dictionary import dict1

# Prompt the user for key-value pair
key = input("Enter a key: ")
value = input("Enter a value: ")

# Add the key-value pair to the dictionary
dict1[key] = value

# Save the updated dictionary back to dict.py
with open('dictionary.py', 'w') as file:
    file.write("dict1 = " + json.dumps(dict1, indent=4))

print("Key-value pair added and dictionary updated.")
