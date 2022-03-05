class Students():

    num_of_students = 0                                            #---This is class variable---

    def __init__(self,fname,lname,age,email):                      #---This is Constructor----
        self.f = fname                                             #
        self.l = lname                                             #These are instance variables
        self.a = age
        self.e = email

        Students.num_of_students += 1

    def name(self):                                                 #---This is class method---
        print(f"My name is {self.f} {self.l} and my age is {self.a}")

akash = Students('Akash','Mandana',21,'aakash.mandana26@gmail.com') #---This is Object---
sachin = Students("Sachin","Mandana",22,"sachinm@gmail.com")

print(Students.num_of_students)
# print(akash.f)
akash.name()
Students.name(akash)



