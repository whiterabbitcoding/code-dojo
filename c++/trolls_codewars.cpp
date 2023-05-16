#include <string>
#include <iostream>
using namespace std;

/*
Codewars problem:

https://www.codewars.com/kata/52fba66badcd10859f00097e/solutions/cpp


Most efficient solution:

# include <string>
# include <regex>
std::string disemvowel(std::string str)
{
  std::regex vowels("[aeiouAEIOU]");
  return std::regex_replace(str, vowels, "");
}

*/


std::string disemvowel(const std::string& str){
string output = "";
string vowels = "aeiou";
int length = str.length();
cout << str.length();
{
    // Traverse the string
    for (int i = 0; i < length; i++) {
        bool isFound = vowels.find(str[i]) != string::npos;
        cout << "\nCurrent char is :" << str[i];
        if (isFound){
            cout << "\nGot a vowel: " << str[i];
        } else {
            cout << "\nGot a non vowel: " << str[i];
            output += str[i];
        }

        // output.append(str[i]);
        // Print current character
    }

}
cout << "\nThe output is : " << output;
return output;
}


int main () {
    // should be smstff
    cout << disemvowel("somestuff");

}
