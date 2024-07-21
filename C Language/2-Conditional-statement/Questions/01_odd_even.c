#include <stdio.h>

int main(){

    int number;
    printf("Enter Number: ");
    scanf("%d",&number);

    if(number%2==0){
        printf("%d is even number",number);
    }
    else{
        printf("%d is odd number",number);
    }
}