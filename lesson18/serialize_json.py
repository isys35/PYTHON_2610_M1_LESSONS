import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}



with open("president.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

json_string = json.dumps(data)
print(json_string)