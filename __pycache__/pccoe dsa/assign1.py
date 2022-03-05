#Akash Mandana
#SECOC366
#DSAL Assignment 01

#linear probing class
class linear_probing_hashing:
    def __init__(self,n):
        entry=[0,""]
        self.hash_table=[entry for i in range(n)]
        self.n=n
        def insert(self,phone,name);
        "this function inserts into hashtable using linear probing"
        for i in range(0,self.n):
            index=(phone+1)%self.n
            if self.hash_table[index]==[0,""]:
                self.hash_table[index]=[phone,name]
                break
            else:
                continue
            def find(self,phone):
                print("Search using linear probing method")
                comparisons=0
                for i in range(0,self.n):
                    index=(phone+i)%self.n
                    if self.hash_table[index][0]==phone:
                        print("Phone no",self.hash_table[index][0])
                        print("Name"self.hash_table[index][1])
                        index=(phone+1)%self.n
                        if self.hash_table[index][0]==phone:
                            print("phone no",self.hash_table[index][0])
                            print("Name",self.hash_table[index][1])
                            print("Comparisons required",index+1)
                            break
                        else:
                            continue
                        print()
                        def print_hashtable
