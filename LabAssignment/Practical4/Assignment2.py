import numpy as np

A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,3))

print("Matrix A\n",A)
print("Matrix B\n",B)

print("Addition\n",A+B)

print("Multiplication\n",A@B)