#include<stdio.h>

//Sum and Average

int main(){

double num1,num2,num3;
double avg,sum;

printf("Enter 3 numbers seperated by a space: ");
scanf("%lf%lf%lf",&num1,&num2,&num3);

sum=num1+num2+num3;
avg=sum/3;

printf("The sum is: %f\n",sum);
printf("The average is: %f",avg);



}