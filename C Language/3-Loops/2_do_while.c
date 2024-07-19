// How do...while loop works?

// The body of do...while loop is executed once. Only then, the (condition) is evaluated.

// If (condition) is true, the body of the loop is executed again and (condition) is evaluated once more.

// This process goes on until (condition) becomes false.

// If (condition) is false, the loop ends.

# include<stdio.h>

int main(){

    // int i = 0;
    // do{
    //     printf("%d ",i);
    //     i++;
    // }
    // while(i<=5);
    
    int coundown = 3;
    do{
        printf("%d ",coundown);
        coundown--;
    }
    while(coundown>=1);
    printf("Happy New Year!");


    // reverse number 
    // int number = 12345;
    // int revnumber = 0;

    // while(number){
    //     revnumber = revnumber*10 + number%10;
    //     number = number/10;
    // }  
    // printf("\nReverse Number is: %d",revnumber);
}