import numpy as np 

#1
def arr_replace(arr):
    res = np.array(arr)
    res[res%2==1] = 0
    return res

#2
def arr_replace_where(arr):
    return np.where(arr%2==0,0,arr)


#3
def arr_repeat(arr):
    return np.repeat(arr,3)

#4
def arr_join(arr):
    res = np.array(arr)
    return np.tile(res,3)

#5
def arr_intersection(arr1,arr2):
    return np.intersect1d(arr1,arr2)

#6
def arr_random(a,b):
    return np.random.uniform(5,10,size=(a,b))