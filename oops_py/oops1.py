class Mandana :
    # def __init__(self, aname,aage,arole) -> None:
        # print(f"Name is {self.aname} Age is {self.aage} an role is {self.arole}")
    life_goal = "Entrepreneurship"  
    # def printDetails(self) :
        #  return (f"Name is {self.name} , age is {self.age} and role is {self.role}")
    
    def __init__(self,aname,aage,arole) :
        self.name = aname
        self.age = aage
        self.role = arole
        
        print (f"Name is {self.name} , age is {self.age} and role is {self.role}")


akash = Mandana("Akash",22,"Programmer")
sachin = Mandana("Sachin",22,"businessman")
# akash.name = "Akash"
# akash.age = 22
# akash.role = "Programmer"
# sachin.name = "Sachin"
# sachin.age = 22
# sachin.role = "Buisnessman"
print(akash.life_goal)
print(akash.role)

