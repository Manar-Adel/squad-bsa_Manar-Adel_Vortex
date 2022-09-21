#Individual Projects on lists, tupples, and if statements

def square(height):
    print("SQUARE:")
    for i in range(1,height+1):
        for j in range(1,height+1):
            if j==1 or j==height or i==1 or i==height:
                print("* ",end="")
            else:
                print("* ",end="")
        print("")

def triangle(height):
    print("TRIANGLE:")
    for i in range(height+1):
        for j in range(i):
            print('*',end="")
        print("")
      
      
def circle(radius):
    print("CIRCLE:")
    for i in range(-radius,radius+1):
        for j in range(-radius,radius+1):
            if i**2 + j**2 == radius**2:
                print('*',end="")
            else:
                print(" ",end="")
        print("")

def pyramid(height):
    print("PYRAMID:")
    for i in range(height):
        j=i
        while j<height:
            print(" ",end="")
            j=j+1
        j=i
        while j>0:
            print('*',end="")
            j=j-1
        j=i
        while j>=0:
            print('*',end="")
            j=j-1
        print("")

def draw_shape(lst):
    
    for i in lst:

            shape=i[0]
            if shape.lower()=="square":
                square(i[1])
            
            elif shape.lower()=="triangle":
                triangle(i[1])
            
            elif shape.lower()=="pyramid":
                pyramid(i[1])

            elif shape.lower()=="circle":
                circle(i[1])    
                          

print("DRAW A SHAPE!")
print("You can enter a square, a triangle, or a pyramid")
num_of_shapes=int(input("Enter the number of shapes you will add:"))
count=0
lst=[] #initial list is empty
while(count<num_of_shapes):
    shape=input("Enter a shape: ")
    height=int(input("Enter a height: "))
    lst.append((shape,height)) #enter a shape and height and store it in a tupple in a list
    count=count+1

lst.sort(key=lambda i:i[1]) #sort them according to height in ascending order
print(lst)
draw_shape(lst)


