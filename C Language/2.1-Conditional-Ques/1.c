// Write a C program to find maximum between two numbers.

# include <stdio.h>

int main(){
    int num1 = 11;
    int num2 = 12;

    if (num1>num2){
        printf("%d is greater than %d",num1,num2);
    }
    else if (num1==num2){
        printf("Both numbers are equal");
    }
    else{
        printf("%d is lesser than %d",num1,num2);
    }
}