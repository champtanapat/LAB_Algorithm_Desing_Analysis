def bubbleSort(arr): 
  n = len(arr)
  for i in range(n-1): 
    print("Iterators : ",i)
    for j in range(0, n-i-1): 
      print("comparison  : ",j)
      if arr[j] > arr[j+1] : 
        arr[j], arr[j+1] = arr[j+1], arr[j]

data  = [14, 33, 27, 35, 10]
data  = [64, 34, 25, 12, 90]
size = len(data)
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)
