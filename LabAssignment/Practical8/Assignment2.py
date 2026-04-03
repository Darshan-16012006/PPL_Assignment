src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

f1 = open(src,"r")
f2 = open(dest,"w")

for line in f1:
    if not line.strip().startswith("#"):
        f2.write(line)

f1.close()
f2.close()

print("File copied without comments.")