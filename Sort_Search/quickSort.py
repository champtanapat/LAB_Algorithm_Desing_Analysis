def partition(arr, low, high):
  i = (low-1)
  pivot = arr[high] #pivot 

  for j in range(low, high):
    # If current element is smaller than or
    # equal to pivot
    if arr[j] <= pivot:
      # increment index of smaller element
      i = i+1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i+1], arr[high] = arr[high], arr[i+1]

  return (i+1)

def quickSort(arr, low, high):
  if len(arr) == 1:
    return arr
  if low < high:
    # pi is partitioning index, arr[p] is now
    # at right place
    pi = partition(arr, low, high)
    # Separately sort elements before
    # partition and after partition
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)


#arr = [10, 7, 8, 9, 1, 5]
arr = [10, 80, 30, 90, 40,50,70]
arr = [34,8,64,51, 32,21,10,25,9,36]
arr = [5,20,2,33,45]
arr = [35,33,42,10,14,11,27,44,26,31]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])