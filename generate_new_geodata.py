import json

countries = ["denmark", "sweden", "norway"]

def main():

    with open("world.geojson") as f:

        data = json.load(f)
        features = data["features"]
        new_data = []

        for elem in features:
            if elem["properties"]["ADMIN"].lower() in countries:
                new_data.append(elem)
        
        data["features"] = new_data

        with open("new-geodata.geojson", "w") as new_file:
            json.dump(data, new_file, indent=6)

main()