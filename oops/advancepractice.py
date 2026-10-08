# program 1

import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        print("area of the circle is:",(math.pi*math.pi*self.radius))

    def parimeter(self):
        print("Parameter of the circle is :",2*math.pi*self.radius)


c1=Circle(5)
c1.Area()
c1.parimeter()


#  Program 2

class Employee:
    def __init__(self,role,department,sale):
        self.role=role
        self.department=department
        self.sale=sale

    def ShowDetails(self):
        print(self.role,self.department,self.sale)


class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("a","b",90)

eng1=Engineer("c",90)

eng1.ShowDetails()

# program 3-Dender function

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price

ord1=Order("chips",60)
ord2=Order("tea",10)
print(ord1>ord2)

    





        
