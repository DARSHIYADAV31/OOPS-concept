class garment:
    count=0    
    def __init__(self,i,t,m,q,price):
        self.id=i
        self.type=t
        self.material=m
        self.qty=q
        self.price=price
        self.id=int(input("Enter Garment ID : "))
        garment.count+=1
    def display(self):
        print("Hello All")
        print(" ID = %d\n Type = %s "%(self.id,self.type))

while True:
    print("1.Input")
    print("2.Display")
    print("3.Exit")
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        obj=garment(101,"Shirt","Cotton",10,1800)
    elif ch==2:
        #obj1=garment(102,"Trouser","Other",2,750)
        obj.display()
    elif ch==3:
        break
    else:
        print("Total Number of Object Used = ",garment.count)
