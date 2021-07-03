def selectionsort(array):
    for i in range(len(array)-1):
        a=i
        for j in range(i,len(array)):
            if array[j] < array[a]:
                a=j
        b=array[i]
        array[i]=array[a]
        array[a]=b
    print(array)

array=[4,7,2,5,9,8,3]
selectionsort(array)