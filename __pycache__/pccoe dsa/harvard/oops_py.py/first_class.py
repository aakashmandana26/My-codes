class Mandana :
    life_goal = "Entrepreneurship"
    pass

akash = Mandana()                                                    
sachin = Mandana()              
akash.name = "Akash"                
sachin.name = "Sachin"              
akash.age = 22              
sachin.age = 22
akash.role="Programmer"             
sachin.role="Businessman"
print(f"Name is {akash.name} and age is {sachin.age}")
print(akash.__dict__)
print(sachin.__dict__)
print(Mandana.__dict__)

print(f"Life goal of Akash is {akash.life_goal}")
sachin.life_goal = "CEO"
print(f"Life goal of Mandana family is {Mandana.life_goal}")
print(f"Life goal of Sachin is {sachin.life_goal}")
