cities = {
    "Lagos": 14800000,
    "Cairo": 10200000,
    "Kinshasa": 17000000,
    "Nairobi": 4700000,
    "Johannesburg": 5600000
}

# convert to list
city_list = list(cities.items())

# sort manually using loop (beginner friendly)
for i in range(len(city_list)):
    for j in range(i + 1, len(city_list)):
        if city_list[i][1] < city_list[j][1]:
            city_list[i], city_list[j] = city_list[j], city_list[i]

print("Top 3 largest cities:")
for i in range(3):
    print(city_list[i][0], "-", city_list[i][1])