import json

with open("data.json", "r") as file:
    my_settings = file.read()
    
data = json.loads(my_settings)
print(data["headless"])