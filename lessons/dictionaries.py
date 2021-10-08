"""Demonstrations of dictionary capabilites."""


# declaring the type of a dictionary
schools: dict[str, int]

# initialize ot empy dictionary
schools = dict()

# set a key-value pairing in dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print dictionary literal
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair froma dictionary, by its key
schools.pop("Duke")

# test for existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

print(schools)

# Update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# emtpy dictionary literal
schools = {}
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])
# Example looping over keys of a dict
for key in schools: 
    print(f"Key: {key} -> Value: {schools[key]}")