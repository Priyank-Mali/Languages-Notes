#include <iostream>
using namespace std;

int main(){

    int number,sum=0;
    bool flag = true;

    do{
        cout<<"Enter a Number: ";
        cin>>number;

        if(number<0){
            flag = false;
            continue;
        }
        sum = sum + number;
    }
    while(flag);

    cout<<"The sum is: "<<sum;
}