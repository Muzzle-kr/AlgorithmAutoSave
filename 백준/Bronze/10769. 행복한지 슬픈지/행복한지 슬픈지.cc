#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    string emoji = "";

    int happy_count = 0, sad_count = 0;

    for (int i = 0; i < s.length(); i++) {
        char c = s[i];

        if (c == ':') {
            emoji = c;
        }

        if (c == '-' and emoji == ":") {
            emoji += c;
        }

        if (c == ')' and emoji == ":-") {
            happy_count++;
            emoji = "";
        }

        if (c == '(' and emoji == ":-") {
            sad_count++;
            emoji = "";
        }
    }

    if (happy_count == 0 and sad_count == 0) {
        cout << "none" << endl;
        return 0;
    }

    if (happy_count == sad_count) {
        cout << "unsure" << endl;
        return 0;
    }

    if (happy_count > sad_count) {
        cout << "happy" << endl;
    } else {
        cout << "sad" << endl;
    }
    return 0;
}