/**
 * Take posotive integer input and tell if it is a three digit number or not
 */

#include <stdio.h>

int main(){

    int number;
    printf("Enter Number: ");
    scanf("%d",&number);

    if(number>99 && number<1000){
        printf("The Number is Three digit number");
    }
    else{
        printf("The Number is Two digit number");
    }
}