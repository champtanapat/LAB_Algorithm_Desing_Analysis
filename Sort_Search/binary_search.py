def binary_search(arr, low, high, x): 
  if high >= low: 
    mid = (high + low)//2 
    if arr[mid] == x: 
      return mid 
    elif arr[mid] > x: 
      return binary_search(arr, low, mid - 1, x) 
    else:  
      return binary_search(arr, mid + 1, high, x) 
  else:
    return -1
data  = [10,14, 27, 27, 35]
size = len(data)
print('Binary Search:')
print(binary_search(data,0,5,10))
print(binary_search(data,0,5,35))

