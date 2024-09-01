#include <iostream>
using namespace std;

int main(){
    /*
    while(condition){
        // code
    }
    */

    // int num = 1;

    // while(num<=10){
    //     cout<<num<<" ";
    //     num++;
    // }
    // return 0;

    /*
    program to find the sum of positive numbers
    if the user enters a negative number, the loop ends 
    the negative number entered is not added to the sum
    */
   int number,sum=0;

    cout<<"Enter a Number: ";
    cin>>number;

    while(number>0){
        sum = sum + number;

        cout<<"Enter a Number: ";
        cin>>number;
    }
    cout<<"The sum is: "<<sum;
}
