class BinaryTree:
    count=0
    def __init__(self,root):
        self.root=root
        self.lch=None
        self.rch=None

    def insertion(self,value):
        if value>=self.root:
            if self.rch:

              self.rch.insertion(value)
            else:
                self.rch=BinaryTree(value)
                BinaryTree.count+=1
        else:
            if self.lch:

                self.lch.insertion(value)
            else:
                self.lch=BinaryTree(value)
                BinaryTree.count += 1

    def pre_order(self):
        print(self.root)
        if self.lch:
            self.lch.pre_order()
        if self.rch:
            self.rch.pre_order()

    def post_order(self):
        if self.lch:
            self.lch.post_order()
        if self.rch:
            self.rch.post_order()
        print(self.root)

    def in_order(self):
        if self.lch:
            self.lch.in_order()
        print(self.root)
        if self.rch:
            self.rch.in_order()

    def isPresent(self,val):
        if(val>self.root):
            if self.rch:
                self.rch.isPresent(val)
            else:
                print ("Value is not present")
                return
        if (val < self.root):
            if self.lch:
                self.lch.isPresent(val)
            else:
                print ("Value is not present")
                return
        if(val==self.root):
            print(f'Value {self.root} is present:)')
            return self.root

    def del_node(self,val):
        parent=self
        temp=self
        while True:

            if(val>temp.root):
                if temp.rch!=None:
                    parent=temp
                    temp=temp.rch
                else:
                    return
            else:
                if(val < temp.root):
                    if temp.lch != None:
                        parent = temp
                        temp = temp.lch
                    else:
                        return
                else:

                    break



        if temp.rch==None and temp.lch==None:
            if parent==temp:
                return None
            if parent.lch==temp:
                parent.lch==None
            else:
                parent.root==None
            return

        if temp.lch==None:
            if parent == temp:
                self.root=temp.rch
                return
            if parent.lch==temp:
                parent.lch=temp.rch
            else:
                parent.rch=temp.rch

            return

        if temp.rch == None:
            if parent == temp:
                self.root = temp.lch
                return
            if parent.lch == temp:
                parent.lch = temp.lch
            else:
                parent.rch = temp.lch
            return


        minitemp=temp.lch
        if minitemp.rch==None:
            minitemp.rch=temp.rch
        else:
            while(minitemp.rch!=None):
                minip=minitemp
                minitemp=minitemp.rch

            minip.rch = minitemp.lch
            minitemp.rch=temp.rch
            minitemp.lch=temp.lch


        if(temp==parent):
            self.root=temp
            return

        if parent.lch==temp:
            parent.lch=minitemp
        else:
            parent.rch=minitemp

        return

b1=BinaryTree(8)
b1.insertion(3)
b1.insertion(18)
b1.insertion(1)
b1.insertion(7)
b1.insertion(28)
b1.insertion(12)
b1.insertion(30)
b1.insertion(26)
b1.insertion(13)
b1.insertion(14)

b1.del_node(18)
b1.pre_order()








