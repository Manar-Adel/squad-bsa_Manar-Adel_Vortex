from abc import abstractmethod
from multiprocessing.connection import wait
from operator import ne
from sys import hexversion
import cv2
from cv2 import waitKey
from cv2 import sqrt
import numpy as np
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
            side = self.nsides 
            lngth = self.side
            
            for j in range(side):  
                tr.forward(lngth)  
                tr.right(360/side)  
                
                
class Quadrilateral(Polygon): #inherits from polygon
    def __init__(self, side):
        self.side=side

    def area(self):
        a, b = self.sides
        area = a*b
        print('The area of the quadrilateral is %0.2f' %area)
    
    def perimeter(self):
        a, b= self.sides
        perim= (2*a)+(2*b)
        print("The area of the triangle is %0.2f" %perim)       

    def draw (self):
        pass   
    
class Octagon(Polygon): 
    def __init__(self, side):
        self.side=side

    def area(self):
        a, b = self.sides
        area = a*b
        print('The area of the quadrilateral is %0.2f' %area)
    
    def perimeter(self):
        a, b= self.sides
        perim= (2*a)+(2*b)
        print("The area of the triangle is %0.2f" %perim)       

    def draw (self):
        nsides=8
        while nsides>0:
            trt.forward(self.side)
            trt.left(45)
            nsides= nsides-1
                        

class Triangle(Polygon): #inherits from polygon
    def __init__(self, side):
        self.__side=side

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)(s-b)(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
    
    def perimeter(self):
        a, b, c = self.sides
        perim= a+b+c
        print("The area of the triangle is %0.2f" %perim)       

    def draw (self):
        pass
        
        
class Equilateral (Triangle):  
    def _init_(self):
        Polygon._init_(self,3)
    def draw(self):
         trt.forward(self.sides)
         trt.left(120)
         trt.forward(self.sides)
         trt.left(120)
         trt.forward(self.sides)
       
       

class Square(Quadrilateral): 
    def init(self,side) -> None:
        #super().init(typee)
        self.side=side
    def area(self):
        return self.side**2
    def perimeter(self):
        return self.side*4
    def draw(self):
        nsides=4
        while nsides>0:
         trt.forward(self.side)
         trt.right(90)
         nsides=nsides-1
    


class rectangle(Quadrilateral):
    def init(self,length,width) -> None:
        #super().init(typee)
        self.__length=length
        self.__width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
    def draw(self):
         trt.forward(self.length)
         trt.right(90)
         trt.forward(self.width)
         trt.right(90)
         trt.forward(self.length)
         trt.right(90)
         trt.forward(self.width)
         trt.right(90)



class pentagon(Polygon):  #inherits from polygon
    def _init_(self):
        Polygon._init_(self,side)

        def area(self):
            Ap= 5.29508497187* pow(int(self.side),2)
            return  Ap         

        def draw(self):
            nsides= 5
            while nsides>0:
             trt.forward(self.side)
             trt.left(72)
             nsides= nsides-1
             
        
        def perimeter():
            PR= 5* self.side
            return PR


#Manar Adel and Zeina Mohamed

class Hexagon(Polygon):  #inherits from polygon
    def _init_(self):
        Polygon._init_(self,side)
        
        def area(self):
            Ah= (3*sqrt(3))*0.5* pow(int(self.side),2)
            return  Ah      
        def perimeter():
            PR= 6* self.side
            return PR

        def draw(self):
            nsides= 6
            while nsides>0:
             trt.forward(self.side)
             trt.left(60)
             nsides= nsides-1
            
     
     
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
        
    
    elif (shape=='s'):
        side=int(input('enter side length: '))
        sq=Square(side)   
        poly=sq
    elif(shape=='et'):
        side=int(input('enter side length: ')) 
        eqt=Equilateral(side)
        poly=eqt
   
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
        poly.area()
        break
    elif(user_choice=='peri'):
         #call the peri function
         poly.perimeter()
         break
    elif (user_choice=='d'):
        #call draw function
        poly.draw()
        break  
    
    prog_exit_repeat=input("To quit, enter : (q) || To enter another option, enter: (again): ")
        

