
import numpy as np
arr=np.array((4,1,6))
print("dimension=",arr.ndim)
print("shape of the array=",arr.shape)
print("The datatype of array",arr.dtype)
print("maximum of the array=",arr.max(axis=0))
print("minimum of the array=",arr.min(axis=0))
print("cumsum of the array=",arr.cumsum(axis=0))
print("avg =", np.average(arr))
print("transpose array",arr.T)
print("maximum",arr.max())
print("minimun",arr.min())
print("sum",arr.sum())
print(arr.cumsum())
