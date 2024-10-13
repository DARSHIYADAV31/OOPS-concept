#creating class

class Student:
    clg_name = "ABC college"
    #default constructors
    def __init__(self):
        pass


    #parameterized constructors
    def __init__(self,name,marks):
        self.name = name #instance attribute
        self.marks=marks
        print("Adding new student in database !")
    

#creating obj
s1 =  Student("karan",96)
print(s1.name , s1.marks)
s2 =  Student("Daisen",96)
print(s2.name , s2.marks)
print(s2.clg_name)


class Car:
    color="Blue"
    brand="mercedes"

    def welcome(self):
        print("color is : ",self.color)
        print("Brand is : ",self.brand)

        
c = Car()
c.welcome()
print(c.color)
print(c.brand)


