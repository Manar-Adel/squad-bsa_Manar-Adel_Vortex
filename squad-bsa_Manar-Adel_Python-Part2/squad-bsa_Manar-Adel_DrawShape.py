#Individual Projects on lists, tupples, and if statements

def draw_shape(lst,count):
    i=0
    j=0
    x=1
    y=1
    space=1
    for i in lst:
        shape=i[0]
        if shape=="square":
            print("square")
            #wasnt able to draw

        elif shape=="triangle":
            print("triangle")
            #wasnt able to draw
            


        elif shape=="pyramid":
            print("pyramid")
            #wasnt able to draw
                          

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
draw_shape(lst,num_of_shapes)


