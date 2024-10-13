'''class garment:
    def __init__(self):
        print("This is Non Parameterised Constructor")
    def display(self,nm):
        print("Hello",nm)

obj=garment()
obj.display("Darshi")
#print(garment.count)'''

'''
class dept:
    def __init__(self,did,dnm):
        print("This is Parameterised Constructor ")
        self.id=did
        self.name=dnm

    def display(self):
        print("Hello Employee You are Selected with  {1} ID & {0} Dept Name".format(self.id,self.name))

obj=dept(101,"Computer")
obj.display()
'''
'''
built in class attributes
1.__dict__ --> it stores information containing class namespace
2.__doc__  --> documentation
3.__name__ --> class name access
4.__module__ --> access perticular module in which class is defined
5.__bases__ --> it display all base classes
'''
'''
class dept:
    did=1
    dname="Research"
    def __init__(self,name,did,age):
        self.name="Abhyuday"
        self.did=111
        self.age=20
        #print("Constructor 1")
    
        
    def input(self):
        self.did=int(input("Enter Dept ID : "))
        self.dname=input("Enter Dept NAme : ")
    def display(self):
        print(self.did," ",self.dname)

obj=dept("palak",118,39)
print(getattr(obj,"name"))
#setattr(obj,"age",18)
print(getattr(obj,"age"))
print(hasattr(obj,"did"))
#obj.display()
#print(obj.did)
#print(obj.dname)

'''
class dept:
    def __init__(self,did,dname):
        self.did=did
        self.dname=dname
    def disp(self):
        print("Name = %s\nID = %d"%(self.dname,self.did))

if __name__=="__main__":
    obj=dept(1,"Sales")
    print(obj.__doc__)
    print(obj.__dict__)
    print(obj.__module__)
    obj.disp()








        
