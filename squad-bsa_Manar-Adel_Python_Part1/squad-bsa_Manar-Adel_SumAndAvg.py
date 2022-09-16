from math import *
from statistics import *
#Sum and Average

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))
sum=num1+num2+num3
avg=(sum)/3
num_lst=[num1,num2,num3]
avg_lst=mean(num_lst)

print("Sum is: "+str(sum))
print("Average without the built in function is: "+str(avg)) #without the built in function
print("Average with the built in function is: "+str(avg_lst)) #with the built in function