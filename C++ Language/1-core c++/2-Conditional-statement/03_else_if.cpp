#include <iostream>
using namespace std;

int main(){

    int marks;

    cout<<"Enter Your Marks: ";
    cin>>marks;

    if(marks>90){
        cout<<"Good";
    }
    else if(marks<=90 && marks>=70){
        cout<<"Average";
    }
    else{
        cout<<"Bad";
    }
}