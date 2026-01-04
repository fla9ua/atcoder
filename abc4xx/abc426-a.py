x, y = input().split()

os = {"Ocelot": 1, "Serval": 2, "Lynx": 3}
print("Yes") if os[x] >= os[y] else print("No")
