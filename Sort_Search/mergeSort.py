def mergeSort(arr):
  if len(arr) >1: 
    mid = len(arr)//2 # Finding the mid of the array 
    L = arr[:mid] # Dividing the array elements 
    R = arr[mid:] # into 2 halves 
    mergeSort(L) # Sorting the first half 
    mergeSort(R) # Sorting the second half 


    i = j = k = 0 

    # Copy data to temp arrays L[] and R[] 
    while i < len(L) and j < len(R): 
      if L[i] < R[j]:
        arr[k] = L[i] 
        i+= 1 
      else: 
        arr[k] = R[j] 
        j+= 1 
      k+= 1 

      # Checking if any element was left 
    while i < len(L): 
        arr[k] = L[i] 
        i+= 1 
        k+= 1 

    while j < len(R): 
        arr[k] = R[j] 
        j+= 1 
        k+= 1


 
data = [12, 11, 13, 5, 6, 7]
data = [21, 38, 29, 17, 4, 25,32,9]
#data = [2,6,5,1,7,4,3]
#data = [40,10,30,25,20]
data = [2,4,1,6,8,5,3,7]
print("Merge Sort")
mergeSort(data)
print("Sorted array is: ", end="\n")
print(data)



