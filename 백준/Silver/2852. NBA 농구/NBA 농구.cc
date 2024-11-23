#include <iomanip>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;
int first_team_winning_seconds;
int second_team_winning_seconds;
int first_team_score = 0;
int second_team_score = 0;

int convertToSeconds(string time) {
    int minutes, seconds;
    char delimiter;

    stringstream ss(time);
    ss >> minutes >> delimiter >> seconds;

    return minutes * 60 + seconds;
};

string convertToMinutes(int seconds) {
    stringstream ss;
    int minutes = seconds / 60;
    int secs = seconds % 60;

    ss << setw(2) << setfill('0') << minutes <<
        ":"
        << setw(2) << setfill('0') << secs;
    return ss.str();
}

int main() {
    int n;
    cin >> n;
    cin.ignore();

    vector<int> numbers;
    vector<string> times;


    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        stringstream ss(line);
        int number;
        string time;

        ss >> number >> time;
        numbers.push_back(number);
        times.push_back(time);
    }

    numbers.push_back(0);
    times.push_back("48:00");

    for (int i = 0; i <= n; i++) {
        int additional_seconds = convertToSeconds(times[i]) - convertToSeconds(times[i - 1]);

        if (first_team_score > second_team_score) {
            first_team_winning_seconds += additional_seconds;
        } else if(first_team_score < second_team_score) {
            second_team_winning_seconds += additional_seconds;
        }

        if (numbers[i] == 1) {
            first_team_score++;
        } else if (numbers[i] == 2) {
            second_team_score++;
        }
    }

    cout << convertToMinutes(first_team_winning_seconds)  << endl;
    cout << convertToMinutes(second_team_winning_seconds) << endl;
}