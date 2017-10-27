import numpy as np
from get_acc import main

print(main())

def convert(arr):
    data = np.array(arr)
    return data

data = convert(raw_data)

data2 = main()
data2 = convert()

print(data)

print(data2)

np.save('test.npy', data)