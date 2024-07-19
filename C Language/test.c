#include <stdio.h>

int main(){

    /**
     * String
     */

    
    char name[10];
    printf("\nEnter Yor name: ");
    scanf("%s",&name);

    printf("Hello, %s How Are You?",name); // this will not give full line of text

    //------------------( to print full text ) --------------------
    // -------------------( fgets() and puts()) ------------------------

    while(getchar()!='\n');
    char nam[20];
    printf("\nEnter Yor name: ");
    fgets(nam,sizeof(nam),stdin); // read entire text

    printf("Nam: ");
    puts(nam);

}