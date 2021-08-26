def sorty(l,i):
    index=i
    if 2*i+2< len(l) and l[2 * i + 2]>l[index]:
        index=2*i+2
    if 2*i+1<len(l) and l[2*i+1]>l[index]:
        index=2*i+1
    if index!=i:
        l[index],l[i]=l[i],l[index]
        sorty(l,index)

def deliver(l):
   for i in range(int((len(l)-1)/2-1),-1,-1):
       sorty(l,i)

def increase_key1(l,i,val):
    l[i]=val
    while i>0:
        ind = int((i - 1) / 2)
        if l[i]>l[ind]:
            l[i],l[ind]=l[ind],l[i]
            i=ind
        else: return

def HeapSorty(l):
    d=[]
    while(len(l)!=0):
        d.append(l[0])
        l.remove(l[0])
        sorty(l,0)
    return d

mass=[2,3,5,2,5,7,5,1,9,5,1,4,3,7,6,5,8]
deliver(mass)
print(mass)
increase_key1(mass,3,8)
print(mass)
k=HeapSorty(mass)
print(k)