nums = tuple(map(int, input("Enter numbers separated by space: ").split()))

print("Total items:", len(nums))
print("Last item:", nums[-1])
print("Reverse order:", nums[::-1])

if 5 in nums:
    print("Yes")
else:
    print("No")

temp = list(nums)
temp.pop(0)
temp.pop(-1)

temp.sort()

print("Remaining sorted items:", temp)