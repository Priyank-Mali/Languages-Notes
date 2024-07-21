/**
 * Take 3 positive integers input and print the greatest of them
 */

#include <stdio.h>

int main(){
    int n1,n2,n3;

    printf("Enter Three Numbers seprated by comma: ");
    scanf("%d,%d,%d",&n1,&n2,&n3);

    if(n1>n2 && n1>n3){
        printf("%d is greatest among three numbers",n1);
    }
    else if(n2>n3 && n2>n1){
        printf("%d is greatest among three numbers",n2);
    }
    if(n3>n2 && n3>n1){
        printf("%d is greatest among three numbers",n3);
    }

}