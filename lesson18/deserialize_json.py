import json

json_str = """
{
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
"""

with open("president.json", "r") as json_file:
    president = json.load(json_file)

print(president)
print(type(president))

print(json.loads(json_str))
print(type(json.loads(json_str)))