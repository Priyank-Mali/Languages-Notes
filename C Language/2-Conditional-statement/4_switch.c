# include<stdio.h>

// switch Statement
// The switch statement allows us to execute one code block among many alternatives.

// You can do the same thing with the if...else..if ladder. However, the syntax of the switch statement is much easier to read and write.


int main(){

   int day = 11;

   switch (day){
    case 1:
        printf("Monday");
        break;
    case 2:
        printf("Tuesday");
        break;
    case 3:
        printf("Wednesday");
        break;
    case 4:
        printf("Thrusday");
        break;
    case 5:
        printf("Friday");
        break;
    case 6:
        printf("Saturday");
        break;
    case 7:
        printf("Sunday");
        break;
    default:
        printf("Invalid Day");
        break;
   }
}