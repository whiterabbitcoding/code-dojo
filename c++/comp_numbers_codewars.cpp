#include <string>
#include <iostream>
using namespace std;

/*
Codewars:

https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de/solutions/cpp

Optimal:

std::string compare(unsigned short a, unsigned short b){
  int d = std::max((a % 10 == b % 10) + (a / 10 == b / 10), (a % 10 == b / 10) + (a / 10 == b % 10));
  return std::to_string(50*d) + "%";
}
*/


std::string compare(unsigned short a, unsigned short b){
  //write your solution here
    std::string as = std::to_string(a);
    std::string bs = std::to_string(b);
    int length = as.length();
    int similar = 0;
    string output = "";
    {
    // Traverse the string
      for (int i = 0; i < length; i++) {
        cout << "\nAS = " << as[i] << "BS = " << bs[i];

        bool isFound = as.find(bs[i]) != string::npos;
        cout << "\nIS found : " << isFound;
        if (isFound) {
          cout << "\n\nposition of bs[i] is : " << as.find(bs[i]);

          as.erase(as.find(bs[i]), as.find(bs[i])+1); // remove bs[i] from the string
          cout << "\n as : " << as;
          similar += 1;
        }
        }
      }

    switch(similar){
      case 0:
        output = "0%";
        break;
      case 1:
        output = "50%";
        break;
      case 2:
        output = "100%";
        break;

    }
    return output;
    }


int main () {
    // should return "50%"
    cout << compare(14,12);
    cout << compare(22,23);
    cout << compare(51,15);
    cout << compare(33,33);
    return 0;
}
