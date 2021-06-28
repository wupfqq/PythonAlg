'''HASHES'''

class Hash:
    def hash_function(self,size,key):
        return key%size

'''Hash with chains'''
class Hash_chains(Hash):
    def __init__(self, size):
        self.hash_table=[[] for _ in range(size)]
    def insert_value(self,value):
        value_key=self.hash_function(len(self.hash_table),value)
        self.hash_table[value_key].append(value)
    def printy(self):
        for x in range(len(self.hash_table)):
            print(x, end=") ")
            for y in self.hash_table[x]:
                print(' -> ',y,end=" ")
            print()

"Jumping_hash"
class Jumping_Hash(Hash):
    def __init__(self,s):
        self.size=s
        self.hash_table=[0 for x in range(s)]
    def insert_value(self,value):

        for jump in range(self.size-1):
            val_l = self.hash_function(self.size, value+jump)
            if not self.hash_table[val_l]:
                self.hash_table[val_l]=value
                return
    def printy(self):
        for y in range(self.size):
            print(y,") ",self.hash_table[y])


my_hash1=Jumping_Hash(15)
my_hash1.insert_value(12)
my_hash1.insert_value(90)
my_hash1.insert_value(67)
my_hash1.insert_value(666)
my_hash1.insert_value(567)
my_hash1.insert_value(671)
my_hash1.insert_value(777)
my_hash1.insert_value(780)
my_hash1.insert_value(9)
my_hash1.insert_value(8)
my_hash1.printy()
