#include<stdio.h>

//Better Calculator

void calc(double num1, char op, double num2){

    

    if(op=='+')
        printf("Answer: %f",num1+num2);
    else if(op=='-')
        printf("Answer: %f",num1-num2);
    else if (op=='*')
        printf("Answer: %f",num1*num2);
    else if (op=='/'){
         if(num2==0)
            printf("INVALID"); //divide by zero exception
         else
            printf("Answer: %f",num1/num2); 
}
    else
        printf("INVALID\n");

}


int main(){

    double num1, num2;
    char op;

    printf("Enter the first number: ");
    scanf("%lf",&num1);
    printf("Enter an operator: ");
    scanf(" %c",&op);
    printf("Enter the second number: ");
    scanf("%lf",&num2);

    calc(num1,op,num2);
}