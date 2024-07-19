#include <stdio.h>

// * 
// * *
// * * *
// * * * *

int main(){

    int x=4;

    for(int i=1;i<=x;i++){
        for(int j=1;j<=i;j++){
            printf("* ");
        }
        printf("\n");
    }

    /**
     * with extra variable
     */
    
    int a=1;
    for(int i=1;i<=x;i++){
        for(int j=1;j<=a;j++){
            printf("* ");
        }
        a++;
        printf("\n");
    }

// A
// A B
// A B C
// A B C D

    for(int i=1;i<=x;i++){
        for(int j=1;j<=i;j++){
            printf("%c ",j+64);
        }
        printf("\n");
    }

// 1
// 1 2
// 1 2 3
// 1 2 3 4

    for(int i=1;i<=x;i++){
        for(int j=1;j<=i;j++){
            printf("%d ",j);
        }
        printf("\n");
    }

// 1
// 2 3
// 4 5 6
// 7 8 9 10

    int a=1;
    for(int i=1;i<=x;i++){
        for(int j=1;j<=i;j++){
            printf("%d ",a);
            a++;
        }
        printf("\n");
    }

// A
// B C
// D E F
// G H I J

    int n=65;
    for(int i=1;i<=x;i++){
        for(int j=1;j<=i;j++){
            printf("%c ",n);
            n++;
        }
        printf("\n");
    }

}