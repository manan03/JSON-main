import json
from CF_dictionary import dict1


def transformit(json_string2):
    # Read the JSON file
    # with open('temp1.json') as file:
    #     json_data = json.load(file)

    # # Convert JSON to string
    # json_string2 = json.dumps(json_data)


    for key, value in dict1.items():
        json_string2 = json_string2.replace('"'+key+'"', '"'+value+'"')

    # print(json_string)

    def string_to_json_file(json_string2, file_path):
        # Convert the JSON string back to a Python object
        json_data = json.loads(json_string2)

        # Write the JSON data to a file
        with open(file_path, 'w') as file:
            json.dump(json_data, file, indent=4)

        return file_path

    output_file = 'temp2.json'
    json_file_path = string_to_json_file(json_string2, output_file)
    print("JSON file created as temp2.json")

    return json_string2
