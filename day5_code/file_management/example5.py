import json


with open("json_data_valid.json") as f:
    file_content = f.read()
    print(f"file content:\n{file_content}")
    print(f"type: {type(file_content)}")

    print(f"file_content[0]: {file_content[0]}")

    json_data_structured = json.loads(file_content)

    print(f"json_data_structured[0]: {json_data_structured[0]}")

