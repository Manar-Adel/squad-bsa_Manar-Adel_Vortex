#include<stdio.h>

//Pyramid

int main(){

    /*take input from the user, the input is a number representing the height of a pyramid, 
    then you need to draw the pyramid based on the user's input (min-height 2 max 5). 
    make use of Arrays for saving the shapes you need to draw and think about the solution,*/

    int height;

    printf("Enter the height: ");
    scanf("%d",&height);



    if(height>=2 && height<=5){
        for(int i=1;i<=height;i++){
            for(int space=1;space<=(height-i);space++){
                printf(" ");
            }
            for(int j=1;j<=(2*i-1);j++){
                printf("*");
            }
            printf("\n");
        }

    }
    else{
        printf("IV=NVALID! The number MUST be between 2 and 5.");
    }


}