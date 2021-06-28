'''BinaryHeap'''
class BinHeap:
    def __init__(self,a):
        self.arr=a
        self.arr.sort(reverse=True)
    def ShiftUp(self,index):
        while(index>0):
            ind_father=int((index-1)/2)
            if self.arr[index]<self.arr[ind_father]:
                return
            self.arr[index],self.arr[ind_father]=self.arr[ind_father],self.arr[index]
            index=ind_father
    def ShiftDown(self,index,value):
        self.arr[index]=value
        while(index<len(self.arr)-1):
            rchild=index*2
            lchild=index*2+1
            if(self.arr[index]>self.arr[rchild] and self.arr[index]>self.arr[lchild]):
                return
            if(self.arr[index]<self.arr[lchild]):
                self.arr[index],self.arr[lchild]=self.arr[lchild],self.arr[index]
                index=lchild
            else:
                if (self.arr[index] < self.arr[rchild]):
                    self.arr[index], self.arr[rchild] = self.arr[rchild], self.arr[index]
                    index=rchild

    def Insert(self,element):
        self.arr.append(element)
        self.ShiftUp(len(self.arr)-1)
    def printy(self):
        for x in self.arr:
            print(x, end=" ")



a=[12,23,4,19,333]
myheap=BinHeap(a)
myheap.Insert(67)
myheap.ShiftDown(1,90)
myheap.printy()