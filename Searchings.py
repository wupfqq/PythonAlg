def BinarySearching(arr,key):
    arr=sorted(arr)
    i=0
    j=len(arr)-1
    while(i!=j):
        mid = (i+j) // 2
        if arr[mid]<key:
            i=mid+1
        if arr[mid]>key:
            j=mid-1
        if key==arr[mid]:
            return key
    raise Exception

print(BinarySearching([1,7,4,2,8,0,5],7))






