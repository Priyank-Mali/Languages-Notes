/*
What is a variable in c?

A variable in C is a named location (or container) in memory that is used to store data which can be used during program execution.

syntax:

type variablename = value

The equal sign is used to assign a value to the variable.

// Declare a variable
int myNum;

// Assign a value to the variable
myNum = 15;
*/

#include<stdio.h>

int main(){

    int myNum = 15;
    char mychar = 'A'; 
    printf("Hello, World!\n");
    // printf(myNum);
    printf("%d",myNum);
    printf("\nmy character is %c and my number is %d",mychar,myNum);
    printf("\nmy character is %c and my number is %d",'B',20);

    // int x = 5, y = 6 , z = 10;
    int x,y,z;
    // x=10,y=11,z=13;
    x=y=z=10;
    printf("\n\"x\"->%d,\"y\"->%d,\"z\"->%d",x,y,z);

    int studentID = 1;
    int studentAge = 99;
    float studentPercentage = 35.53;
    char studentGrade = 'C';

    printf("\nStudent ID: %d",studentID);
    printf("\nStudent Age: %d",studentAge);
    printf("\nStudent Percentage: %.2f",studentPercentage);
    printf("\nStudent Grade: %c",studentGrade);

    // int a = 10;
    // printf("\n%d",a++);
    // printf("\n%d",++a);

}


/*
In many other programming languages (like Python, Java, and C++), 
you would normally use a print function to display the value of a variable. 
However, this is not possible in C:

To output variables in C, you must get familiar with something called "format specifiers".

Format Specifiers:
Format specifiers are used together with the printf() function to tell the compiler what type of data the variable is storing. It is basically a placeholder for the variable value.

A format specifier starts with a percentage sign %, followed by a character.

%d or %i -> int 
%f or %F -> float
%lf -> double
%c -> char
%s -> strings

*/

