from abc import abstractmethod
from multiprocessing.connection import wait
from operator import ne
from sys import hexversion
import cv2
from cv2 import waitKey
from cv2 import sqrt
import math
import turtle as trt

#ALL TEAM MEMBERS 

#Habiba Ahmed and Mohamed Maghraby

class Polygon: #base class
    
    @abstractmethod
    def  area():
        pass
    @abstractmethod
    def  perimeter():
        pass        
    @abstractmethod
    def draw(self):
            tr = trt.Turtle()
            trt.TurtleScreen._RUNNING=True  
            side = self.nsides 
            lngth = self.side
            for j in range(side):  
                tr.forward(lngth)  
                tr.right(360/side)  
                
                
class Quadrilateral(Polygon): #inherits from polygon
    def __init__(self, side1,side2):
        self.side1=side1
        self.side2=side2

    def area(self):
        a=self.side1
        b=self.side2
        area = a*b
        print(f'The area of the quadrilateral is {area}')
    
    def perimeter(self):
        a, b= self.sides
        perim= (2*a)+(2*b)
        print(f"The perimeter of the Quadreral is {perim}")       

    def draw (self):
        pass   
    
class Octagon(Polygon): 
    def __init__(self, side):
        self.side=side

    def area(self):
        areaa=0
        areaa = 2*(1+math.sqrt(2))*self.side**2
        print(f'The area of the Octagon is {areaa}')
    
    def perimeter(self):
        a, b= self.sides
        perim= (2*a)+(2*b)
        print("The area of the Octagon is %0.2f" %perim)       

    def draw (self):
        trt.TurtleScreen._RUNNING=True
        
        nsides=8
        while nsides>0:
            
            trt.forward(self.side*10)
            trt.left(45)                        

class Triangle(Polygon): #inherits from polygon
    def __init__(self, side1,side2):
        self.side1=side1
        self.side2=side2
    def area(self):
        area=0
        base=self.side2
        height=self.side1
        area = (math.sqrt(height**2 - (base*0.5)**2))*base*0.5
        print('The area of the triangle is ',area)
    
    def perimeter(self):
        perim=0
        if (self.side1==self.side2):perim= self.side1*3
        else:perim=self.side2+2*self.side1
        print("The perimeter of the triangle is",perim)       

    def draw (self):
        pass
        
        
class Equilateral (Triangle):  
    def __init__(self,sides):
        self.sides=sides
    def draw(self):
        while self.sides >0:
            trt.forward(self.sides*10)
            trt.left(120)
            
class isoceles(Triangle):  
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2
    def draw(self):
        while self.side1 >0:
            trt.forward(100) # draw base
            trt.left(120)
            trt.forward(100)
            trt.left(120)
            trt.forward(100)
            trt.penup()
            trt.right(150)
            trt.forward(50)         
       
       

class Square(Quadrilateral): 
    def __init__(self,side) -> None:
        #super().init(typee)
        self.side=side
    def draw(self):
        nsides=4
        while nsides>0:
            trt.forward(self.side*10)
            trt.right(90)
            
    


class rectangle(Quadrilateral):
    def __init__(self,length,width) -> None:
        self.length=length
        self.width=width
    def draw(self):
        while self.length>0:
            trt.forward(self.length*10)
            trt.right(90)
            trt.forward(self.width*10)
            trt.right(90)         
class pentagon(Polygon):  #inherits from polygon
    def __init__(self,side):
        self.side=side
    def area(self):
        Ap= 5.29508497187* pow(int(self.side),2)
        print("The area of pentagon is",Ap)         
    def draw(self):
        nsides= 5
        while nsides>0:
            trt.forward(self.side*10)
            trt.left(72)    
    def perimeter(self):
        PR= 5* self.side
        print("The peremiter of pentagon is",PR)

#Manar Adel and Zeina Mohamed

class Hexagon(Polygon):  #inherits from polygon
    def __init__(self,side):
        self.side=side
        
    def area(self):
        Ah= (3*sqrt(3))*0.5*pow(int(self.side),2)
        return  Ah      
    def perimeter(self):
        PR= (6)*(self.side)
        return PR

    def draw(self):
        nsides= 6
        while nsides>0:
            trt.forward(self.side*10)
            trt.left(60)
             
            
     
     
#MENU
#The user will select which polygon to compute its area or perimeter or to draw it. Try to make this available as a menu choice. (done)
#Ask the user whether he wants to quit the program or enter an option again. (done)
#Every user input must be validated by the application. Ask the user to enter the correct information if it is incorrect until the user gets it right. (use while loop) (done)

side=0
side1=0
side2=0

print("Which polygon do you want to draw?")
print("----------------------------------")
shape=""
prog_exit_repeat="again"
#while((shape!="et" and shape!="it" and shape!="s" and shape!="r" and shape!="p" and shape!="h" and shape!="o" )): #loops until the user eneters the correct info
#    print("Triangle: (Equilateral Triangle: et ), (Isosceles Triangle : it)")   
#    print("Quadrilateral: (Square: s) , (Rectangle: r)")      
#    print("(Pentagon: p) , (Hexagon: h) , (Octagon: o)")  
    
   
   
#call the constructor and add sides to it   

while prog_exit_repeat!="q" and prog_exit_repeat=="again": 
    
    print("Triangle: (Equilateral Triangle: et ), (Isosceles Triangle : it)")   
    print("Quadrilateral: (Square: s) , (Rectangle: r)")      
    print("(Pentagon: p) , (Hexagon: h) , (Octagon: o)")  
    shape=input("Enter here: ")
    
    if(shape=='r'):
        side1=int(input("enter side 1: "))
        side2=int(input('enter side 2: '))
        rec=rectangle(side1,side2)
        poly=rec
    
    elif (shape=='s'):
        side=int(input('enter side length: '))
        sq=Square(side)   
        poly=sq
    elif(shape=='et'):
        side=int(input('enter side length: ')) 
        eqt=Equilateral(side)
        poly=eqt
    elif(shape=='it'):
        print("Put the equal sides First")
        side1=int(input('enter side length 1: '))
        side2= int(input('enter side length 2: '))
        
        iso=isoceles(side1,side2)
        poly=iso
    elif (shape=='p'):
        side=int(input('enter side length: '))  
        pen=pentagon(side) 
        poly=pen
    elif(shape=='h'):
        side=int(input('enter side length: ')) 
        hexa=Hexagon(side)  
        poly=hexa
    elif(shape=='o'):
        side=int(input('enter side length: '))  
        octa=Octagon(side)
        poly=octa
        
    else:
        print("Triangle: (Equilateral Triangle: et ), (Isosceles Triangle : it)")   
        print("Quadrilateral: (Square: s) , (Rectangle: r)")      
        print("(Pentagon: p) , (Hexagon: h) , (Octagon: o)")    
        
        
        
        
    user_choice=input("to calculate area (a), to calculate perimeter (peri), to draw (d): ")     
    if(user_choice=='a'):
        #call the area function
        if type(poly)==rectangle:
            poly=Quadrilateral(side1,side2)
            poly.area()
        elif type(poly)==Square:
            poly=Quadrilateral(side,side)
            poly.area()
        elif type(poly)==isoceles:
            poly=Triangle(side1,side2)
            poly.area()
        elif type(poly) == Equilateral:
            poly=Triangle(side,side)
            poly.area()
        else:
            poly.area()
        
        break
    elif(user_choice=='peri'):
         #call the peri function
        if type(poly)==rectangle:
            poly=Quadrilateral(side1,side2)
            poly.perimeter()
        elif type(poly)==Square:
            poly=Quadrilateral(side,side)
            poly.perimeter()
        elif type(poly)==isoceles:
            poly=Triangle(side1,side2)
            poly.perimeter()
        elif type(poly) == Equilateral:
            poly=Triangle(side,side)
            poly.perimeter()
        else:
            poly.perimeter()
        
        break
    elif (user_choice=='d'):
        #call draw function
        try:
            poly.draw()
        except Exception:
            prog_exit_repeat=input("To quit, enter : (q) || To enter another option, enter: (again): ")
