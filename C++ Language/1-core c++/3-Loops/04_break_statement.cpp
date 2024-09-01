#include <iostream>
using namespace std;

int main()
{
    // for(int i=1;i<=5;i++){
    //     if(i==4){
    //         break;
    //     }
    //     cout<<i<<" ";
    // }

    /*
    program to find the sum of positive numbers
    if the user enters a negative numbers, break ends the loop
    the negative number entered is not added to sum
    */
    int number,sum=0;

    while(true){
        cout<<"Enter a Number: ";
        cin>>number;

        if(number<0){
            break;
        }

        sum = sum + number;
    }

    cout<<"The sum is: "<<sum;
}