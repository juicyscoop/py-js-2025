import json
json_data = []
with open("data.csv") as f:
    lines = f.readlines()
    data = []
    columns = lines[0].strip("\n").split(",")
    for i in lines[1:]:
        row = i.strip("\n").split(",")
        data_row = {
            columns[0]: row[0],
            columns[1]: row[1],
            columns[2]: row[2],
        }
        json_data.append(data_row)

print(f"json_data: \n {json_data}")

json_dumped = json.dumps(json_data)
print(json_dumped)

with open("json_data_valid.json", "w") as f:
    f.write(json_dumped)




