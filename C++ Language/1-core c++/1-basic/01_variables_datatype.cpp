#include <iostream> // header file
using namespace std;
/*
C++ supports the following data types:

Primary or Built-in or Fundamental data type
Derived data types
User-defined data types

1. Primitive Data Types: These data types are built-in or predefined data types and can be used directly by the user to declare variables. example: int, char, float, bool, etc. Primitive data types available in C++ are: 

Integer
Character
Boolean
Floating Point
Double Floating Point
Valueless or Void
Wide Character

2. Derived Data Types: Derived data types that are derived from the primitive or built-in datatypes are referred to as Derived Data Types. These can be of four types namely: 

Function
Array
Pointer
Reference

3. Abstract or User-Defined Data Types: Abstract or User-Defined data types are defined by the user itself. Like, defining a class in C++ or a structure. C++ provides the following user-defined datatypes:  

Class
Structure
Union
Enumeration
Typedef defined Datatype

*/

/*
Syntax:

datatype variablename = value;
*/

int main(){

    cout<<"Hello                           world"<<endl;

    /**
     * INTEGER ----------------------------------------------------
     */

    int num1 = 10;
    int num2 {20};
    // int num2(30); 

    int num3 = 0;
    int num4 {};

    int a = 10.3;  // print(10)
    cout<<"a: "<<a<<endl;

    // int floatnum {10.2}; error
    // cout<<"floatnum: "<<floatnum<<endl;

    int floatnum(10.2);    // print(10)
    cout<<"floatnum: "<<floatnum<<endl;


    cout<<"num1: "<<num1<<endl;
    cout<<"num2: "<<num2<<endl;
    cout<<"num3: "<<num3<<endl;
    cout<<"num4: "<<num4<<endl;

    /**
     * FLOAT -------------------------------------------------
     */

    float n1 = 10.2; // precision : 7
    float n2{10.2};
    
    cout<<"n1: "<<n1<<endl;
    cout<<"n2: "<<n2<<endl;

    // float // precision : 7
    // double  // precision : 15+
    // long double // precision : 15++

    /**
     * BOOLEAN (True / False)---------------------------------------------
     */


    bool flag = true;

    if(flag){
        cout<<"The Flag is green: "<<endl;
    }
    else{
        cout<<"The Flag is Green";
    }


    /**
     * CHARACTER -------------------------------------------------
     */

    char char1 = 'a';
    cout<<"char1 :"<<char1<<endl;

    char value = 65;
    cout<<"value: "<<value<<endl;

    /**
     * STRING --------------------------------------------------
     */

    string greeting = "hello";
    cout<<"greeting: "<<greeting<<endl;

    string name = "priyank mali";
    cout<<"name: "<<name<<endl;

    /**
     * CONSTANT --------------------------------------------
     */
    const int x = 12;
    cout<<"x: "<<a<<endl;

    // x = 20; error

    /**
     * NAN ---------------------------------------------
     */
    double nu1 = 0;
    double nu2 = 0;

    cout<<"nu1/nu2: "<<nu1/nu2<<endl;

    /**
     * INFINITY ----------------------------------------------
     */
    float numb1 = 3.4;
    float numb2 = 0;

    cout<<"numb1/numb2 :"<<numb1/numb2<<endl;

    return 0;
}

/*
Errors and Warnings in c++:

1.) Compile Time Error(syntax error)
    std::cout<<"hello world"<<std::endl
    error of ;


2.) Runtime Errors
    divided by zero ( 11/0 )
    invalid input
    uninitialized variables


3.) Warnings
    highlight areas where your code where there might be bugs
*/