#include <stdio.h>

// C break
// The break statement ends the loop immediately when it is encountered.

// C continue
// The continue statement skips the current iteration of the loop and continues with the next iteration.

int main(){
    /**
     * WAP to calculate the sum of numbers
     * if user enters a negative numbers, the loop terminates
     */

    int num,sum=0;
    for(int i=1;i<=10;i++){
        printf("Enter Number%d: ",i);
        scanf("%d",&num);

        if(num<0){
            break;
        }
        sum = sum + num;
    }
    printf("Sum: %d",sum);


    /**
     * WAP calculate the sum of numbers (10 numbers max)
    * If the user enters a negative number, it's not  added to the result
     */

    int number,sum=0;

    for(int i=1;i<=10;i++){
        printf("Enter Number%d: ",i);
        scanf("%d",&number);

        if(number<0){
            continue;
        }
        sum += number;
    }

    printf("Sum: %d",sum);

}