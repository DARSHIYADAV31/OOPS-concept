'''
class dept:
    did=1
    dname="Research"
    def __init__(self,name,did,age):
        self.name="Abhyuday"#dname
        self.did=111#did
        self.age=20#dage
        #print("Constructor 1")
    
        
    def input(self):
        self.did=int(input("Enter Dept ID : "))
        self.dname=input("Enter Dept NAme : ")
        self.age=int(input("ENter Age : "))
    def display(self):
        print(self.did," ",self.dname," ",self.age)

obj=dept("palak",118,39)
#print(getattr(obj,"name"))
#setattr(obj,"age",18)
#print(getattr(obj,"age"))
#print(hasattr(obj,"did"))
#obj.input()
obj.display()
#print(obj.did)
#print(obj.dname)
'''
class garment:
    def __init__(self,gid,gtype,gmat,gq,gp):
        self.id=0
        self.type="null"
        self.matirial="null"
        self.quantity=0
        self.price=0
    def input(self):
        self.id=int(input("ENter ID : "))
        self.type=input("Enter Type : ")
        self.matirial=input("ENter Matirial : ")

    def display(self):
        print(self.id," ",self.type," ",self.matirial)


obj=garment(101,"Shirt","Cotton",10,1400)
obj.input()
obj.display()
