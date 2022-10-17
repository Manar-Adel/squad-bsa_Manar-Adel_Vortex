from abc import abstractmethod
from multiprocessing.connection import wait
from operator import ne
import cv2
from cv2 import waitKey
from cv2 import sqrt
import numpy as np
import turtle as turt

class Polygon: #base class
    def __init__(self,nsides ):
        self.nsides=nsides
        self.sides=[0 for i in range(nsides)]
        def inputSides(self):
            self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.nsides)]

    @abstractmethod
    def  area():
        pass
    @abstractmethod
    def  perimeter():
        pass        
    @abstractmethod
    def draw(self):
            tr = turt.Turtle()  
            side = self.nsides 
            lngth = self.side
            
            for j in range(side):  
                tr.forward(lngth)  
                tr.right(360/side)  
                
                
class Quadrilateral(Polygon): #inherits from polygon
    def __init__(self):
        Polygon.__init__(self,4)

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

class Triangle(Polygon): #inherits from polygon
    def __init__(self):
        Polygon.__init__(self,3)

    def area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
    
    def perimeter(self):
        a, b, c = self.sides
        perim= a+b+c
        print("The area of the triangle is %0.2f" %perim)       

    def draw (self):
        pass
        
        
class Equilateral (Triangle):  #inherits from triangle
    def __init__(self):
        Polygon.__init__(self,3)
    def draw(self):
        a, b, c = self.sides
        h= (a+b+c)/2
        row=0
        while row<h:
            space= h- row-1
            while space>0:
                print(end=" ")
                space=space-1
            star = row+1
            while star>0:
                print("*",end=" ")
                star=star-1
            row= row+1
            print()
            

class Square(Quadrilateral): #TO BE DONE
    def _init_(self,side) -> None:
        #super()._init_(typee)
        self.side=side
    def area(self):
        return self.side**2
    def perimiter(self):
        return self.side*4
    def draw(self):
        for i in range(0,self.side):
            print("* ",end="")
        print("")
        for i in range(0,self.side-2):
            print("*",end="")
            for y in range(0,self.side*2-3):
                print(" ",end="")
            print("*")
        print("",end="")
        for i in range(0,self.side):
            print("* ",end="") 


class rectangle(Quadrilateral): #TO BE DONE
    def _init_(self,length,width) -> None:
        #super()._init_(typee)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimiter(self):
        return (self.length+self.width)*2
    def draw(self):
        for i in range(0,self.width):
            print("* ",end="")
        print("")
        for i in range(0,self.length-2):
            print("*",end="")
            for y in range(0,self.width*2-3):
                print(" ",end="")
            print("*")
        print("",end="")
        for i in range(0,self.width):
            print("* ",end="")



class pentagon(Polygon):  #inherits from polygon
    def __init__(self):
        Polygon.__init__(self,5)

        def area(self):
            Ap= 5.29508497187* pow(int(self.side),2)
            return  Ap         

        def draw(self):
            super.draw(self)
        
        def perimeter():
            PR= 5* self.side
            return PR

class Hexagon(Polygon):  #inherits from polygon
    def __init__(self):
        Polygon.__init__(self,6)
        
        def area(self):
            Ah= (3*sqrt(3))*0.5* pow(int(self.side),2)
            return  Ah      
        def perimeter():
            PR= 6* self.side
            return PR

        def draw(self):
            super.draw(self)
            
     
     
#MENU
#The user will select which polygon to compute its area or perimeter or to draw it. Try to make this available as a menu choice. (done)
#Ask the user whether he wants to quit the program or enter an option again. (done)
#Every user input must be validated by the application. Ask the user to enter the correct information if it is incorrect until the user gets it right. (use while loop) (done)



print("Which polygon do you want to draw?")
print("----------------------------------")
shape=""
prog_exit_repeat="again"
while((shape!="et" and shape!="it" and shape!="s" and shape!="r" and shape!="p" and shape!="h" and shape!="o" ) or (prog_exit_repeat!="q" and prog_exit_repeat=="again")): #loops until the user eneters the correct info
    print("Triangle: (Equilateral Triangle: et ), (Isosceles Triangle : it)")   
    print("Quadrilateral: (Square: s) , (Rectangle: r)")      
    print("(Pentagon: p) , (Hexagon: h) , (Octagon: o)")  
    shape=input("Enter here: ")
    prog_exit_repeat=input("To quit, enter : (q)) || To enter another option, enter: (again): ")

               