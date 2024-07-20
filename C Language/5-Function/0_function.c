#include <stdio.h>

/*
Functions
A function is a block of code that performs a specific task.

Suppose, you need to create a program to create a circle and color it. You can create two functions to solve this problem:

create a circle function
create a color function
Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.
*/

/**TYPE:
 * 
 * Standard Library Function
 * User-defined Function
 */

int addNumbers(int a , int b){
    int result;
    result = a+b;
    return result;
}


int main(){

    int n1,n2,sum;

    printf("Enter Two Numbers Sepratd by Comma: ");
    scanf("%d,%d",&n1,&n2);

    sum = addNumbers(n1,n2);
    printf("Sum: %d",sum);
}