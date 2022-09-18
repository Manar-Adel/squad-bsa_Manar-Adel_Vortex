#Better Calculator

def calc(num1,num2,op):
    if op =="+":
        print(num1+num2)
    elif op =="-":
     print(num1-num2)
    elif op =="*":
        print(num1*num2)    
    elif op =="/":
        if num2==0:
            print("INVALID") #DIVIDE BY XERO EXCEPTION
        else:   
            print(num1/num2)    
    else:
        print("INVALID OPERATOR")



num1=float(input("Enter the first number: "))
op=input("Enter the operator: ")
num2=float(input("Enter the second number: "))

calc(num1,num2,op)      