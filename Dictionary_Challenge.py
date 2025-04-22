# Create a dictionary

thisDict = {"brand": "Jaguar", "model": "XK8", "year": 1997}
thisDict
{'brand': 'Jaguar', 'model': 'XK8', 'year': 1997}

# Get() method

x = thisDict.get("model")
print(x)

# Update() method

thisDict.update({"year": 2001})
print(thisDict)
{'brand': 'Jaguar', 'model': 'XK8', 'year': 2001}

# Add Items

thisDict["color"] = "carnival red"
print(thisDict)
{'brand': 'Jaguar', 'model': 'XK8', 'year': 2001, 'color': 'carnival red'}
# Nested Dictionary

thisDict = {"car1" :{ "brand": "Jaguar", "model": "XK8", "year": 1997}, "car2": {"brand": "Land Rover", "model": "Defender", "year": 2025}, "car3": {"brand": "Volkswagen", "model": "GTI", "year": 2023}}
print(thisDict)
{'car1': {'brand': 'Jaguar', 'model': 'XK8', 'year': 1997}, 'car2': {'brand': 'Land Rover', 'model': 'Defender', 'year': 2025},'car3': {'brand': 'Volkswagen', 'model': 'GTI', 'year': 2023}}

# Fromkeys() Method

thisdict = dict.fromkeys(x)
print(thisdict)
{'key1': None, 'key2': None, 'key3': None}
