import overpass

def find_nearby_cafes(latitude, longitude):
    api = overpass.API()
    query = f"""
    node["amenity"="cafe"](around:1000,{latitude},{longitude});
    out;
    """
    response = api.get(query)
    if "features" in response:
        return response["features"]
    else:
        return []

def main():
    latitude = 18.5204  # Pune city center latitude
    longitude = 73.8567  # Pune city center longitude

    cafes = find_nearby_cafes(latitude, longitude)

    if cafes:
        print("Nearby Cafes:")
        for index, cafe in enumerate(cafes, start=1):
            name = cafe.get("properties", {}).get("name", "Unnamed Cafe")
            print(f"{index}. {name}")
    else:
        print("No nearby cafes found.")

if __name__ == "__main__":
    main()


# """
#     import overpass

# def find_nearby_cafes(latitude, longitude):
#     api = overpass.API()
#     query = f"""
#     node["amenity"="cafe"](around:1000,{latitude},{longitude});
#     out;
#     """
#     response = api.get(query)
#     return response

# def main():
#     latitude = 18.5204  # Pune city center latitude
#     longitude = 73.8567  # Pune city center longitude

#     response = find_nearby_cafes(latitude, longitude)
    
#     if "elements" in response:
#         cafes = response["elements"]
#         if cafes:
#             print("Nearby Cafes:")
#             for index, cafe in enumerate(cafes, start=1):
#                 name = cafe.get("tags", {}).get("name", "Unnamed Cafe")
#                 print(f"{index}. {name}")
#         else:
#             print("No nearby cafes found.")
#     else:
#         print("Error: Unexpected response from Overpass API")
#         print(response)

# if __name__ == "__main__":
#     main()

# """