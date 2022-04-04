def selectionSort (array, size) :
    for i in range(size-1):
        minimum = i
        for  j in range(i+1 , size)  :
            if array[j] < array[minimum]:
                minimum = j 
        #swap(array[minimum], array[ i])
        #(array[i], array[minimum]) = (array[minimum], array[i])
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp 

data  = [-2, 45, 0, 11, -9]
data  = [14, 33, 27, 35, 10]
size = len(data)
selectionSort(data , size)
print('Sorted Array in Ascending Order:')
print(data)
        