// goto Statement
// The goto statement allows us to transfer control of the program to the specified label.

// syntax

// goto lable;

// lable:
//     statement


#include <stdio.h>

int main(){

// Program to calculate the sum and average of positive numbers
// If the user enters a negative number, the sum and average are displayed.
    const int maxInput = 100;
    int i;
    float sum = 0, avg, count = 0;
    for(i=1;i<=maxInput;i++){
        printf("Enter Number%d: ",i);
        scanf("%d",&maxInput);

        if(maxInput<0){
            goto jump;
        }
        sum += maxInput;
        count += 1;

    }
    jump:
        // count = (i-1);
        printf("The sum is: %.2f",sum);
        printf("\nThe Average is: %f",sum/count);

}

// quote from Bjarne Stroustrup, creator of C++, "The fact that 'goto' can do anything is exactly why we don't use it."