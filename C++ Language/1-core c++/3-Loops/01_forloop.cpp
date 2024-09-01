#include <iostream>
using namespace std;

int main(){

    /*
    for(initialization; condition; increment/decriment){
        // body of loop
    }
    */
    // for(int i=1;i<10;i++){
    //     cout<<i<<" ";
    // }

    // for(int i=1;i<=5;i++){
    //     cout<<"Hello World"<<endl;
    // }

    /*
    C++ program to find the sum of first n natural numbers
    positive integers such as 1,2,3,...n are known as natural numbers
    */

    int num,sum=0;

    cout<<"Enter Range of N naturale numbers: ";
    cin>>num;

    for(int i=1;i<=num;i++){
        sum = sum + i;
    }
    cout<<"The sum of "<<num<<" natural number is: "<<sum;

}