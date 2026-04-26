#include <iostream>
using namespace std;

int main() {
    double num1;
    double num2;
    long long result;
    char op;
    cout<<"*************CALCULATOR*************"<<endl;
    cout<<"Enter #1: ";
    cin >> num1;
    cout<<"Enter operator(+,-,*,/)";
    cin >> op;
    cout<<"Enter #2: ";
    cin >> num2;

    switch(op){
        case '+':
        long long result = num1 + num2;
        cout<< "Result: " <<result<<endl;
        cout<<"************************************";
        break;
        case '-':
        result = num1 - num2;
        cout<< "Result: " <<result<<endl;
        cout<<"************************************";
        break;
        case '*':
        result = num1 * num2;
        cout<< "Result: " <<result<<endl;
        cout<<"************************************";
        break;
        case '/':
        result = num1 / num2;
        cout<< "Result: " <<result<<endl;
        cout<<"************************************";
        break;
        default:
        cout<<"Use only +,-'*'/"<<endl;
        cout<<"************************************";
        break;
        
    }
}
