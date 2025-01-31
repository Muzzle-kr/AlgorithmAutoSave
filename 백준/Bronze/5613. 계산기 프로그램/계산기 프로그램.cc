#include <iostream>
#include <vector>

using namespace std;

int calculate(int a, int b, char op) {

    if (op == '+') {
        return a + b;
    } else if(op == '-') {
        return a - b;
    } else if(op == '*') {
        return a * b;
    } else if(op == '/') {
        return a / b;
    } else {
        return 0;
    }
}

int main() {
    int idx = 0;
    int answer = 0;
    char op;

    while (true) {
        string s;
        cin >> s;

        if (s == "=") {
            break;
        }

        if (idx % 2 == 0) {
            if (idx == 0) {
                answer = stoi(s);
            } else {
                answer = calculate(answer, stoi(s), op);
            }
        } else {
            op = s[0];
        }
        
        idx++;
    }

    cout << answer << endl;
    return 0;
}