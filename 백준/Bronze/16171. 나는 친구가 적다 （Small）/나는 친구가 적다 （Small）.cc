#include <iostream>
#include <string>

using namespace std;

int main() {
    string input;
    cin >> input;

    string find_word;
    cin >> find_word;

    string result = "";

    for (char ch : input) {
        if (!isdigit(ch)) {
            result += ch;
        }
    }

    if (result.find(find_word) != string::npos) {
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }
    return 0;
}
