#include <stdio.h>

int main(){

    /**
     * Integer / float
     */
 
    int num;
    printf("Enter Number: ");
    scanf("%d",&num);
     
    printf("The Numner is: %d",num);

    /**
     * Character
     */

    // clear the input buffer before reading a character
    while(getchar() != '\n');

    char alpha;
    printf("\nEnter Character: ");
    scanf("%c",&alpha);

    printf("Your character is: %c",alpha);

    /**
     * Multiple Value
     */
    int a;
    float b;

    printf("\nEnter integer and than float: ");
    scanf("%d %f",&a,&b);

    printf("Integer: %d",a);
    printf("\nInteger: %f",b);
    
    return 0;
}