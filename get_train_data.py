import numpy as np
from get_acc import main

def convert(arr):
    data = np.array(arr)
    return data

data2 = main()
print(data2)
d = convert(data2)

# print(d)

# np.save('test.npy', data)