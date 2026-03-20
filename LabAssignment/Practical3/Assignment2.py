items = list(map(int,input("Enter item numbers separated by space: ").split()))

print("Total items:", len(items))

print("Last item:", items[-1])

items.sort()
print("Sorted list:", items)

if 515 in items:
    print("Yes")
else:
    print("No")

items.append(121)
items.append(321)

items.sort()
print("Updated list:", items)