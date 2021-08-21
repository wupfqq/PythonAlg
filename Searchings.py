def BinarySearching(arrt,key):
    arr=sorted(arrt)
    i=0
    j=len(arr)-1
    while(i!=j):
        mid = (i+j) // 2
        if arr[mid]<key:
            i=mid+1
        if arr[mid]>key:
            j=mid-1
        if key==arr[mid]:
            return {key: arrt.index(arr[mid])}
    raise Exception

def LinearSearch(arr,key):
    for x in arr:
        if x==key:
            return {key: arr.index(x)}
    raise Exception



def BinarySearchES(arr,key,i,j):
    while(i!=j):
        mid = (i+j) // 2
        if arr[mid]<key:
            i=mid+1
        if arr[mid]>key:
            j=mid-1
        if key==arr[mid]:
            return "Position in sorted array for number"+str({key: arr.index(arr[mid])})
    return

def ExponentSearch(arr,key):
    arr=sorted(arr)
    index=1
    if arr[0]==key:
        return {key:0}
    while(index<len(arr) and arr[index]<key):
        index*=2
    return BinarySearchES(arr,key,index//2,min(index,len(arr)-1))





print(ExponentSearch([1,7,4,2,8,0,5],7))






