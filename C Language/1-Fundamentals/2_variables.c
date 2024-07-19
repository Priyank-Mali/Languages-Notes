/**
 * Variables:
  
In programming, a variable is a container (storage area) to hold data.

To indicate the storage area, each variable should be given a unique name (identifier). Variable names are just the symbolic representation of a memory location. For example:

    type variablename = value

    int age = 99;

 */


#include<stdio.h>

int main(){

    int myNum = 15;
    char mychar = 'A'; 
    // printf(myNum);

    /*
    In many other programing lanuage (like java / python / c++) , you would manuallu use a print function to display the value of a variable
 
    however, this is not possible in C:

    to output variables in C : --> we use "format specifiers"

    int     -->  %d  or  %i
    float   -->  %f  or  %F
    double  -->  %lf
    char    -->  %c
    string  -->  %s
    */

    printf("%d",myNum);
    printf("\nmy character is: %c",mychar);

    printf("\nmy number is: %d",20);
    printf("\nmy character is: %c",'B');
    
    int x=5,y=10,z=15;
    printf("\nMy name is \"priyank\"");
    printf("\n\"x\"->%d,\"y\"->%d,\"z\"->%d",x,y,z);
    

    int studentID = 1;
    int studentAge = 99;
    float studentPercentage = 35.53;
    char studentGrade = 'C';

    printf("\nStudent ID: %d",studentID);
    printf("\nStudent Age: %d",studentAge);
    printf("\nStudent Percentage: %.2f",studentPercentage);
    printf("\nStudent Grade: %c",studentGrade);

    int a = 10;
    printf("\n%d",a++);
    printf("\n%d",++a);

}


