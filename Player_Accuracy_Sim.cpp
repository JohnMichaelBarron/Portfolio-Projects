/*
Written by John-Michael Barron  
Player Accuracy Simulation

This program generates 25 mock accuracy percentages between 10.0 and 100.0.
The user can choose to view all data, high performers, or overall stats using a switch-case.

Compiled with:
g++ -std=c++17
*/

#include <iostream>
#include <iomanip>
#include <random>
#include <vector>
using namespace std;

// Generate 25 random accuracy values between 10 and 100
void generateAccuracies(vector<double>& accList) {
    random_device rd;                                // True random seed
    default_random_engine gen(rd());                 // Engine
    uniform_real_distribution<> dist(10.0, 100.0);   // Range: 10 to 100

    for (int i = 0; i < 25; ++i) {
        accList.push_back(dist(gen));
    }
}

int main() {
    vector<double> accuracies;
    generateAccuracies(accuracies); // Fill with random accuracy data

    int choice;
    do {
        cout << "\n\t Accuracy Tracker Menu \n";
        cout << "=================================================\n";
        cout << "1. Show all 25 player accuracy values\n";
        cout << "2. Show high performers (90%+)\n";
        cout << "3. Show average accuracy and noob performer\n";
        cout << "4. Exit\n";
        cout << "=================================================\n";
        cout << "Enter your choice(1, 2, 3 or 4): ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "\nAll Accuracy Values:\n";
            for (size_t i = 0; i < accuracies.size(); ++i) {
                cout << "Player " << (i + 1) << ": " 
                     << fixed << setprecision(2) << accuracies[i] << "%\n";
            }
            break;

        case 2:
            cout << "\nHigh Performers (90%+):\n";
            for (size_t i = 0; i < accuracies.size(); ++i) {
                if (accuracies[i] >= 90.0) {
                    cout << "Player " << (i + 1) << ": "
                         << fixed << setprecision(2) << accuracies[i] << "% \n";
                }
            }
            break;

        case 3: {
            double total = 0;
            double lowest = accuracies[0];
            int lowestIndex = 0;

            for (size_t i = 0; i < accuracies.size(); ++i) {
                total += accuracies[i];
                if (accuracies[i] < lowest) {
                    lowest = accuracies[i];
                    lowestIndex = i;
                }
            }
            double average = total / accuracies.size();
            cout << "\nAverage Accuracy: " << fixed << setprecision(2) << average << "%\n";
            cout << "Noob Performer: Player " << (lowestIndex + 1)   // "Noob Performer" just means you need a better mouse. No judgment.
                 << " with " << lowest << "% \n";
            break;
        }
// Maybe upgrade this into a leaderboard with ranks? Future update
        case 4:
            cout << "Exiting tracker. Stay sharp out there!\n";
            break;

        default:
            cout << "Mission Failed. Please try again.\n";
        }

    } while (choice != 4);

    return 0;
}
