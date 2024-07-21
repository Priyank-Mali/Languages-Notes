/**
 * WAP to check Year is Leap year or not.
 */

#include <stdio.h>

int main(){

    int year;
    printf("Enter Year: ");
    scanf("%d",&year);

    if(year%4==0){
        printf("The %d is a leap year",year);
    }
    else{
        printf("The %d is not a leap year",year);
    }
}