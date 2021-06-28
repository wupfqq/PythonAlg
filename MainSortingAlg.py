'''Quicksort :)'''
def Partiton(a,h,t):
    head=h
    tail=t
    pivot=a[int((h+t)/2)]
    while(head<=tail):
        while a[head]<pivot:
            head+=1
        while a[tail]>pivot:
            tail-=1
        if(head<=tail):
            a[head],a[tail]=a[tail],a[head]
            head+=1
            tail-=1

    if tail>h:
        Partiton(a,h,tail)
    if head<t:
        Partiton(a,head,t)
def Quicksort(a):
    if isinstance(a,list):
        Partiton(a,0,len(a)-1)
    else:
        raise TypeError

'''BUBBLE_SORT:]'''
def BubbleSort(a):
    if not isinstance(a,list):
        raise TypeError
    for x in range(len(a)-1):
        for y in range(len(a)-1):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]


'''INSERTION_SORT:>'''
def InsertonSort(a):
    for x in range(1,len(a)):
        for y in range(x-1,-1,-1):
            if a[x]<a[y]:
                temp=a[x]
                for z in range(x-1,y-1,-1):
                    a[z+1]=a[z]
                a[y]=temp


'''Selecton_sort:}'''
def SelectionSort(a):
    for x in range(len(a)-1):
        min=x
        for y in range(x+1,len(a)):
            if a[y]<a[min]:
                min=y
        a[x],a[min]=a[min],a[x]

'''Coctail sort *~* '''
def Coctail_sort(a):
    head=0
    tail=len(a)-1
    while(head<tail):
        for x in range(head,tail):
            if a[x+1]<a[x]:
                a[x+1],a[x]=a[x],a[x+1]
        tail-=1
        for y in range(tail,head,-1):
            if a[y-1]>a[y]:
                a[y-1],a[y]=a[y],a[y-1]
        head+=1



a=[56,12,23,99,65]
Coctail_sort(a)
print(a)

