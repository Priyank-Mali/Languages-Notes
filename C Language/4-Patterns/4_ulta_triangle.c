#include <stdio.h>

int main(){

    int x=4;
    
// * * * * 
// * * *
// * *
// *

    for(int i=1;i<=x;i++){
        for(int j=4;j>=i;j--){
            printf("* ");
        }
        printf("\n");
    }


    for(int i=1;i<=x;i++){
        for(int j=1;j<=x+1-i;j++){
            printf("* ");
        }
        printf("\n");
    }

    
    
}