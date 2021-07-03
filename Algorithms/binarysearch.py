def binarysearch(array,n):
    l=0
    u=len(array)-1
    while l<=u:
        mid=(l+u)//2
        if array[mid]==n:
            return mid
        else:
            if array[mid] < n:
                l=mid+1
            elif array[mid] > n:
                u=mid-1
    return "Not found"
                
array=[1,2,3,4,5,6,7,8,9,10,403,6034,43024]
print("Index:", binarysearch(array,403))