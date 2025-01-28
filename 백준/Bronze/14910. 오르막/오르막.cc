#include <iostream>
#include <vector>
#include <sstream>
#include <climits>

using namespace std;

int main() {
    string line;
    getline(cin, line);

    stringstream ss(line);
    vector<int> numbers;
    int num;

    while (ss >> num) {
        numbers.push_back(num);
    }

    int last_number = INT_MIN;

    for (int i = 0; i < numbers.size(); i++) {
        int current_number = numbers[i];
        if (current_number >= last_number) {
            last_number = current_number;
        } else {
            cout << "Bad" << endl;
            return 0;
        }
    }

    cout << "Good" << endl;
    return 0;
}
