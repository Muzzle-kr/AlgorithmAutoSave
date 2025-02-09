#include <iostream>

using namespace std;

string fizzBuzz(int n) {
    if (n % 3 == 0 && n % 5 == 0) {
        return "FizzBuzz";
    } else if (n % 3 == 0) {
        return "Fizz";
    } else if (n % 5 == 0) {
        return "Buzz";
    } else {
        return to_string(n);
    }
}

bool isDigits(string s) {
    for (char c : s) {
        if (!isdigit(c)) {
            return false;
        }
    }
    return true;
}

int main() {
    int n = 0;

    for (int i = 0; i < 3; i++) {
        string s;
        cin >> s;

        if (isDigits(s)) {
            n = stoi(s) + 3 - i;
        }
    }

    cout << fizzBuzz(n) << endl;
    return 0;
}