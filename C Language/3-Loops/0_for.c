// When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop

# include <stdio.h>

int main(){
    int i;

    // for(initializer ; condition ; increment/decrement){
    //            statement inside the body
    // }
    for(i=0;i<5;i++){
        printf("%d\n",i);
    }


    /**
     * calculate the sum of n natural numbers
     */

    int num,sum=0;

    printf("Enter Number: ");
    scanf("%d",&num);

    for(int i=1;i<=num;i++){
        sum = sum + i;
    }
    printf("Sum of first %d numbers is: %d",num,sum);
}