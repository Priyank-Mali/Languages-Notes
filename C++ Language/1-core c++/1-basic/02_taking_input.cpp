#include <iostream>
#include <string>
using namespace std;

/*
cout --> printing data
cin --> taking input
*/

int main(){
    int num;
    cout<<"Enter a Number: ";
    cin>>num;
    cout<<"The number is: "<<num<<endl;
    
    // add numbers -------------------------------
    int num1,num2;
    cout<<"Enter Number 1: ";
    cin>>num1;
    cout<<"Enter Number 2: ";
    cin>>num2;

    cout<<"The Sum of "<<num1<<" end "<<num2<<" is: "<<num1+num2<<endl;

    // swap numbers -------------------------------
    int a,b;
    cout<<"Enter A: ";
    cin>>a;
    cout<<"Enter B: ";
    cin>>b;
    cin.ignore();
    
    cout<<"Old Number is --> A: "<<a<<" B: "<<b<<endl;

    int c;
    c = a;
    a = b;
    b = c;
    
    cout<<"Swap Number is --> A: "<<a<<" B: "<<b<<endl;

    // take input from user name and age --------------------------
    // int age;
    // string name;

    // cout<<"Enter Your Name: ";
    // cin>>name;
    // cout<<"Enter Your Age: ";
    // cin>>age;

    // cout<<"Hello, "<<name<<" your age is: "<<age<<endl;

    // This will not run when user type name with space so,.... -----------------------

    int age;
    string name;

    cout<<"Enter Your Name: ";
    getline(cin, name);
    cout<<"Enter Your Age: ";
    cin>>age;

    cout<<"Hello, "<<name<<" your age is: "<<age<<endl;

    return 0;
}


/*
    int num1;
    int age;
    string name;

    cout<<"Enter one number: ";
    cin>>num1;
    cin.ignore();
    
    cout<<"Enter Yor name: ";
    getline(cin,name);
    cout<<"Enter your age: ";
    cin>>age;
    
    cout<<"Hello, "<<name<<" your age is: "<<age;
 */


