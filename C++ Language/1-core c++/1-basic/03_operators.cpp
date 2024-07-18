#include <iostream>
using namespace std;

/**
 * Arithmetic (+ , - , * , / , % , ++ , --)
 * Relational (= , += , -= , *= , /= , %= , &= , |= , ^= , <<= , >>=)
 * Logical (&& , || , !)
 * Assignment (== , != , > , < , >= , <=)
 * Bitwise
 * Misc
 */

int main(){

    int a = 10;
    cout<<"a++: "<<a++<<endl; 
    cout<<"++a: "<<++a<<endl;

    cout<<"a--: "<<a--<<endl; 
    cout<<"--a: "<<--a<<endl; 


    /**
     * Misc
     */
    // 1.) sizeof operator

    int x = 10;
    cout<<sizeof(x)<<endl; // 4 byte

    // 2.) turnary operator

    // 3.) comma operator

    int y = (1,2,3);
    cout<<"y: "<<y<<endl;
}