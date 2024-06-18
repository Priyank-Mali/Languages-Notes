// The do/while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.

# include<stdio.h>

int main(){
    /*
    int i = 0;
    do {
        printf("%d\n",i);
        i++;
    }
    while(i<5);
    */
  
   int countdown = 3;
  
   while(countdown>0){
        printf("%d\n",countdown);
        countdown--;
   }
   printf("Happy new year !!");

    // reverse number 
    int number = 12345;
    int revnumber = 0;

    while(number){
        revnumber = revnumber*10 + number%10;
        number = number/10;
    }  
    printf("\nReverse Number is: %d",revnumber);
}