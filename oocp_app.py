#Q2
'''

class hosp:
    name="Darshi"
    id=101

print(hosp.__dict__)
'''
#Q3
'''

class hosp:
    def __init__(self,hid,hname):
        self.hid=hid
        self.hname=hname
    def disp(self):
        print("Name = %s\nID = %d"%(self.hname,self.hid))

if __name__=="__main__":
    obj=hosp(101,"Saraswati")
    print(obj.__dict__)
    

'''
#Q4
'''

import builtins
abs_func = builtins.abs
print(abs_func.__doc__)
absolute_val = abs_func(-155)
print(absolute_val)
'''
#Q5
'''
class student:
    def __init__(self,sid,sname):

        self.sid=sid
        self.sname=sname
        
    def student(self):
        print("Student ID is : ",self.sid)
        print("Student Name is : ",self.sname)


obj=student(1,"Abhi")
obj.student()
'''
#Q6
'''
def student(student_id,**kwargs):
    print(student_id,"***")
    if "student_nm" in kwargs:
        print(kwargs["student_nm"])
    if "student_nm" and "student_cls"in kwargs:
        print(kwargs["student_nm"],"===",kwargs["student_cls"])



student(111,student_nm="Darshi Yadav")
student(121,student_nm="Darshi Yadav",student_cls=15)
'''

#Q7
'''

class Student:
    pass

print(type(Student))

'''

#Q8
'''
class Student:
    def hello():
        print("Hello")

class Marks:
    def hello1():
        print("Darshi")

obj = Student()
objs = Marks()
print(isinstance(obj, Student))
print(isinstance(objs, Marks))

'''















