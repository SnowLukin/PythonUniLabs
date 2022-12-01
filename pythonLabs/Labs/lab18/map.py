import folium
import osmnx as ox


def get_share(name, names):
    freq = names.count(name)
    return freq * 100 / len(names)


def get_names(locations):
    new_locations = []
    for location in locations:
        name = str(gdf[gdf['geometry'] == location]['name'].values[0])
        new_locations.append(name)
    return new_locations


def most_frequent(locations):
    counter = 0
    num = locations[0]

    for location in locations:
        curr_frequency = locations.count(location)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = location

    return num

coordinates = (45.020844611097225, 39.031289040117294)  # current location
m = folium.Map(location=coordinates, zoom_start=13, tiles='openstreetmap')

gdf = ox.geometries_from_point(coordinates, tags={'amenity': 'cafe', 'cuisine': 'coffee_shop'}, dist=10500)

cafes_locations = gdf['geometry'].tolist()   # objects locations

names = get_names(cafes_locations)
most_freq = most_frequent(names)

for cafe_location in cafes_locations:
    print(str(cafe_location))
    if str(cafe_location)[2] == 'I':
        cafe_name = str(gdf[gdf['geometry'] == cafe_location]['name'].values[0])

        color = 'red'
        if cafe_name == most_freq:
            color = 'orange'
        folium.Marker(
            location=[cafe_location.y, cafe_location.x],
            icon=folium.Icon(color=color, icon="map-pin", prefix='fa'),
            popup="<b>" + cafe_name + " " + "{:.2f}".format(get_share(cafe_name, names)) + "%" + str(names.count(cafe_name)) + "</b>"
        ).add_to(m)
m.save('cafes.html')
print('Success')