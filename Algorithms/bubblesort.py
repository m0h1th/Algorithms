def bubblesort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j] > array [j+1]:
                a=array[j]
                array[j]=array[j+1]
                array[j+1]=a
            else:
                continue
    print(array)        
array=[4,7,2,5,9,8,3]
bubblesort(array)
