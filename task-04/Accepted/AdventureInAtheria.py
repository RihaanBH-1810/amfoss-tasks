n = int(input())

cities = list(map(int, input().split()))

if (n < 1 or n > 105) or max(cities) > 110:
    exit() 

k = len(cities)
J = len(set(cities))

m = min(cities)
if cities.count(m)>1:
    print("Still Aetheria")
else:
    pl = min(cities)
    pos = cities.index(pl)
    print(pos + 1)
