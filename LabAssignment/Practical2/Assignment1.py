V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R): "))

I = V / R

print("Current =", I)

if I < 0.5:
    print("Low current")
elif I <= 2:
    print("Normal current")
else:
    print("High current")