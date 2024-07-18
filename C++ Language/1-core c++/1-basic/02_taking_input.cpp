#include <iostream>
using namespace std;

int main(){
    int num;
    cout<<"Enter a Number: ";
    cin>>num;
    cout<<"The number is: "<<num<<endl;
    
    // add numbers
    int num1,num2;
    cout<<"Enter Number 1: ";
    cin>>num1;
    cout<<"Enter Number 2: ";
    cin>>num2;

    cout<<"The Sum of "<<num1<<" end "<<num2<<" is: "<<num1+num2<<endl;

    // swap numbers
    int a,b;
    cout<<"Enter A: ";
    cin>>a;
    cout<<"Enter B: ";
    cin>>b;
    
    cout<<"Old Number is --> a: "<<a<<" b: "<<b<<endl;

    int c;
    c = a;
    a = b;
    b = c;
    
    cout<<"Swap Number is --> a: "<<a<<" b: "<<b;


}