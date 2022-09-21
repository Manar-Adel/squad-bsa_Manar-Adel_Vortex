#Exponent Function

def raise_to_power(base_num,power_num):
    result=1
    for index in range(power_num):
        result*=base_num

    return result    
print("WITHOUT USING BUILT IN FUNCTION:")
print(raise_to_power(2,7))  
print("USING BUILT IN FUNCTION:")  
print(pow(2,7))