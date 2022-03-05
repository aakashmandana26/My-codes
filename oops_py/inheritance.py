class UniversityPeople():

    def __init__(self,fname,lname,age,email,job):                      #---This is Constructor----
        self.f = fname                                             #
        self.l = lname                                             #These are instance variables
        self.a = age
        self.e = email
        self.job = job

    def fullname(self):                                                 #---This is class method---
        print(f"My name is {self.f} {self.l}. Email id: {self.e}")


class Students(UniversityPeople):   #Students class is inheriting from UniversityPeople class
    def __init__(self, fname, lname, age, email, job,semester):
        super().__init__(fname, lname, age, email, job)
        self.sem = semester

    # def __init__(self,job):
        # self.job = "Student"
        

class Teachers(UniversityPeople):   #Teachers class is inheriting from UniversityPeople class
    def __init__(self, fname, lname, age, email, job, salary):
        super().__init__(fname, lname, age, email, job)
        self.sal = salary

class Maths(Teachers):              #Inheritance inside inheritance
    pass             
    
                

      
    

    # def __init__(self,job):
        # self.job = "Teacher"

akash = Students("Akash","Mandana",21,"aakash.mandana26@gmail.com","Student","5th Semester")
harry = Teachers("Harry","Bhai",27,"harry@gmail.com", "Coding Teacher","100000 $")
ashok = Maths("Ashok","Sir",50,"ashusir@gmail.com","Proffessor","10000 $")




# print(akash.job )


akash.fullname()
print(akash.sem)

harry.fullname()
print(harry.sal)

ashok.fullname()
print(ashok.sal)

print(f"akash is an instance of Teachers class: {isinstance(akash,Teachers)}")
print(f"harry is an instance of Teachers class: {isinstance(harry,Teachers)}")
print(f"ashok is an instance of UniversityPeople class: {isinstance(ashok,UniversityPeople)}")

print(f"Maths is a subclass of Teachers class: {issubclass(Maths,Teachers)}")
print(f"Maths is a subclass of UniversityPeople class: {issubclass(Maths,UniversityPeople)}")
print(f"Maths is a subclass of Students class: {issubclass(Maths,Students)}")


#-----------------------------------------Polymorphism----------------------------------------

for people in (akash,harry,ashok):
    people.fullname()

def printage(name):
    print(name.a)

printage(ashok)
printage(akash)
printage(harry)

