#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

for i in range(1,6):
    for j in range(6-i):
        print(i, end=" ")
    print()


#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()