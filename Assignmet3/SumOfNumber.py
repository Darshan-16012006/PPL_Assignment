# sum of all numberbfrom 1 to a given no.
n = int(input("Enter a number: "))
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i += 1

print("Sum =", sum)