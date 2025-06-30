/*
Written by John-Michael Barron
Length Converter with Exception Handling

This program converts lengths from feet and inches to centimeters.
It demonstrates exception handling for invalid (non-numeric or negative) input,
retries only the invalid portion, and uses clean loops for each input segment.

Original try catch ended the program immediately without giving user a second chance, 
didn't feel like that was fair, so I added two do whiles to loop until user
inputs real responses. 

Compiled with:
g++ -std=c++17
*/

#include <iostream>
#include <iomanip>  //precision
#include <string>   //strings!
#include <exception> //custom exception
#include <cctype>    //character handling isdigit tolower

using namespace std;

//non-numeric input exception
class nonNumber : public exception {
public:
    const char* what() const noexcept override {
        return "Invalid input: Go ahead and enter a REAL number.\n";
    }
};

//negative values exception 
class negativeNumber : public exception {
public:
    const char* what() const noexcept override {
        return "Negative values are not allowed for physical lengths.\n";
    }
};

// Helper to check if string is numeric
bool itsANumber(const string& str) {
    if (str.empty()) return false;
    for (char ch : str) {
        if (!isdigit(ch)) return false;
    }
    return true;
}

int main() {
    char again;

    do {
        int feet = 0;
        int inches = 0;
        string input;

        // Loop until valid feet input
        while (true) {
            try {
                cout << "\nEnter the feet portion: ";
                getline(cin, input);

                if (!itsANumber(input)) throw nonNumber();
                feet = stoi(input);
                if (feet < 0) throw negativeNumber();
                break;
            }
            catch (const exception& e) {
                cout << e.what() << "\nTry again.\n";
            }
        }

        // Loop until valid inches input
        while (true) {
            try {
                cout << "Enter the inches portion: ";
                getline(cin, input);

                if (!itsANumber(input)) throw nonNumber();
                inches = stoi(input);
                if (inches < 0) throw negativeNumber();
                break;
            }
            catch (const exception& e) {
                cout << e.what() << "\nTry again.\n";
            }
        }

        // Perform conversion
        double totalInches = feet * 12 + inches;
        double centimeters = totalInches * 2.54;

        cout << fixed << setprecision(2);
        cout << "\nConverted length: " << centimeters << " cm\n";

        // Ask to repeat
        cout << "\nWanna go again? (y/n): ";
        cin >> again;
        cin.ignore(1000, '\n'); // Clean input buffer

    } while (tolower(again) == 'y');

    cout << "\nLater. Don't forget your measuring tape!\n";
    return 0;
}
