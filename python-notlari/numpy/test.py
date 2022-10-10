import numpy as np


number1 = np.arange(6)

number2 = np.arange(20,26)

result1 = number1.reshape(2,3)
result2 = number2.reshape(2,3)


cift = result1 %2 == 0

print(result1)
print(result1[cift])
