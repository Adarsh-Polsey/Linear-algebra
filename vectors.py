# Virtual environment activation
        # source .venv/bin/activate

# importing numpy
import numpy as np
# Declaring vector using list
vector1=[1,2,3,4,5]
vector2=[6,7,8,9,10]
a=np.array(vector1)
b=np.array(vector2)
print(a)

# Adding two vectors
print("Vector Addition "+str(a+b))
# Subtracting two vectors
print("Vector Subtraction "+str(a-b))
# Multiplying two vectors
print("Vector Multiplication "+str(a*b)) 
# Dividing two vectors
print("Vector Division "+str(a/b))

# Dot product of two vectors
print("Dot Product of two vectors "+str(np.dot(a,b)))