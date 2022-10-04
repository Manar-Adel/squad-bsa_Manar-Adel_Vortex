#include<stdio.h>

//Mad Libs Game 

int main(){

char color[20], pluralNoun[20], celebrityF[20], celebrityL[20];

printf("Enter a color: ");
scanf("%s",color);
printf("Enter a plural noun: ");
scanf("%s",pluralNoun);
printf("Enter a celebrity's first and last name: ");
scanf("%s%s",celebrityF,celebrityL);

printf("Roses are %s \n",color);
printf("%s are blue\n",pluralNoun);
printf("I love %s %s\n",celebrityF,celebrityL);


}