cities = []
while True:
    cities.append(input().split())
    cities[-1][1] = int(cities[-1][1])
    if cities[-1][0] == "Waterloo":
        break
city = min(cities, key=lambda x: x[1])
print(city[0])

