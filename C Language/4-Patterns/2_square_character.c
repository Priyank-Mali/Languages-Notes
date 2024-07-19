#include <stdio.h>

// A B C D 
// A B C D
// A B C D
// A B C D

int main(){

    int x=4;

    for(int i=1;i<=x;i++){
        int a=65;
        for(int j=1;j<=x;j++){
            printf("%c ",a);
            a += 1;
        }
        printf("\n");
    }

    printf("\n");

    /**
     * without extra variable
     */
    
    for(int i=1;i<=x;i++){
        for(int j=1;j<=x;j++){
            printf("%c ",j+64);
        }
        printf("\n");
    }

}