import numpy as np
from get_acc import arr

raw_data = arr

def convert(arr):
    data = np.array(arr)
    return data

data = convert(raw_data)
print(data)

np.save('test.npy', data)