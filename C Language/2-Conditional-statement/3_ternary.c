# include<stdio.h>

int main(){

    int marks = 79;
    // variable = (condition) ? expressionTrue : expressionFalse;

    
    marks = (marks>=90) ? printf("A grade") : (marks>=80 && marks<90) ? printf("B grade") : printf("C grade"); 
}