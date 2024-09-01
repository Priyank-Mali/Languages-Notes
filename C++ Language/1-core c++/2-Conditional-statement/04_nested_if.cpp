#include <iostream>
using namespace std;

int main(){

    //  C++ program to find if an integer is positive, negative or zero

    int num;

    cout<<"Enter number: ";
    cin>>num;

    if(num!=0){
        if(num>0){
            cout<<"The Number is positive.";
        }
        else{
            cout<<"The Number is negetive.";
        }
    }
    else{
        cout<<"The number is Zero.";
    }
}