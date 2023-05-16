#include <iostream>
#include <string>
using namespace std;


/*
Commands:
    g++ *file*
    >>
    ./a.out
*/

// This a comment
/* This is a multi
    line comment*/
int main () {
    cout << "Hello World!";
    int myNum = 15;
    // reassign
    myNum = 10;

    double myFloatNum = 5.99;

    char myLetter = 'A';

    string myText = "alex";

    bool aBoolean = false;

    double sum = myFloatNum + myNum;

    cout << sum;

    // declare multiple variables
    int x=1, y=2, z=3;

    int a,b,c;

    a=b=c=10;

    // constant - unchangeable, read only
    const int anotherNum = 1;

    cin >> x;
    cout << "Your number is: " << x;

    // string concatenation

    string firstName = "John ";
    string lastName = "Doe";
    string concat = firstName + lastName;
    cout << concat;
    string fullName = firstName.append(lastName);
    cout << fullName;

    cout << "The length of the firstName strng is " << firstName.length();

    char fourthOfFirstName = firstName[0];

    // returns false
    cout << "\n yo yo " << ( a == b);

    if (a >= b) {
        cout << "a is greater than or equal to b";
    } else {
        cout << "a not greater than or equal to b";
    };

    string result = (a < 18) ? "a less than 18" : "a greater 18";
    cout << result;

    // switch statement
    int day = 4;
    switch (day) {
    case 1:
        cout << "Monday";
        break;
    case 2:
        cout << "Tuesday";
        break;
    case 3:
        cout << "Wednesday";
        break;

    // while loops
    int i = 0;
    while (i < 5) {
        cout << i << "\n";
        i++;
    }

    // for loop - similar to js
    for (int i = 0; i < 5; i++) {
         cout << i << "\n";
    }

    // for-each loop
    int myNumbers[5] = {10, 20, 30, 40, 50};
    for (int i : myNumbers) {
        cout << i << "\n";
    }

    int getArrayLength = sizeof(myNumbers) / sizeof(int);


    // break and continue also works the same as python

    // Create a structure variable called myStructure
    struct {
    int myNum;
    string myString;
    } myStructure;

    // Assign values to members of myStructure
    myStructure.myNum = 1;
    myStructure.myString = "Hello World!";

    // How to show memory address
    string food = "Pizza";
    cout << &food;

    return 0;
}
