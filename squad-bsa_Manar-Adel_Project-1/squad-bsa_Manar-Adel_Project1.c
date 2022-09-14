#include<stdio.h>
#include<math.h>
#include <stdlib.h>


//Square Function: ZEINA MOHAMED
void SquareFunction(int height){
    int i, j;
    for(i=1; i<=height; i++)
    {
        for(j=1; j<=height; j++)
        {
            printf("* ");
        }
        printf("\n");
    } 
}

//Right Triangle Function: MOHAMED AYMAN
void RightTriangleFunction(int height){
     int i, j;
    for(i=1; i<=height; i++)
    {
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        printf("\n");
    }     
}

//Cirlce Function: MANAR ADEL

void CircleFunction(int diameter)
{   
    int i,j;
    double radius= diameter/2;

    for (i=0; i<=diameter; i++)
    {
        for (j=0; j<=diameter; j++)
        {
            double distance = sqrt(pow(i-radius,2) + pow(j-radius,2));
            if (distance>radius-0.5 && distance<radius+0.5)
            {
                printf("*");
            }
            else
            { printf(" ");}
        }
        printf("\n");
    }
}

//Pyramid Function: HABIBA ABBASS
void PyramidFunction(int height){
    if(height>=2){
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
}

//STRUCTS: ZEINA MOHAMED
struct Square
{
    int height;
};
//STRUCTS: MANAR ADEL
struct Circle
{
    int radius;
};
//STRUCTS: HABIBA ABBASS
struct Pyramid
{
    int height;
};
//STRUCTS: MOHAMED AYMAN
struct RightTriangle
{
    int height;
};


// ALL TEAM MEMBERS
int main()
{
    char shape;
    int height;

    struct Square s;
    struct Pyramid p;
    struct RightTriangle r;
    struct Circle c;


    //MANAR ADEL and ZEINA MOHAMED
    printf("Draw a Shape!\n");
    printf("Circle: c, Sqaure: s, Right Triangle: r, Pyramid: p \n");
    printf("Enter a Character: ");
    scanf("%c",&shape);

    //TEST CASE: wrong character
    while(shape!='c' && shape!='s' && shape!='r' && shape!='p'){
        printf("INVALID CHARACTER\n");
        printf("Circle: c, Sqaure: s, Right Triangle: r, Pyramid: p \n");
        printf("Enter a Character: ");
        scanf("%c",&shape);
    }

    //MOHAMED AYMAN and HABIBA ABBASS
    printf("Enter the height: ");
    scanf("%d",&height);

    //TEST CASE: wrong height
    while(height<=0){
        printf("INVALID HEIGHT\n");
        printf("Enter the height: ");
        scanf("%d",&height);
    }

    switch(shape){
        case 's': 
            s.height=height;
            SquareFunction(s.height); break;
        case 'r': 
            r.height=height;
            RightTriangleFunction(r.height); break;
        case 'p': 
            p.height=height;
            PyramidFunction(p.height); break;
        case 'c': 
            c.radius=height;
            CircleFunction(c.radius); break;
        default: printf("INVALID CHARACTER.");
    }
    
    }

    


   




