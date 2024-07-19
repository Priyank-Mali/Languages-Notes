// while(condition)

// if (condition) is true ,statement inside the body of while loop executed.

// The process goes on until (condition) is evaluated to false.
// If (condition) is false, the loop terminates (ends).

# include<stdio.h>

int main(){
    
    int i = 1;

    while(i<=10){
        printf("%d ",i);
        i++;
    }
}