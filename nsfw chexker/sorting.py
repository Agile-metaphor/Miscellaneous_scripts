import json
import os
# Read the JSON data from a file
with open("./data.json", "r", encoding="utf8") as file:
    data = json.load(file)


# Iterate over the data
for file_location, values in data.items():
    if values['hentai'] > 0.5 or values['porn'] > 0.5:
        # Delete the image file
        os.remove(file_location)
        print("Deleted:", file_location)
