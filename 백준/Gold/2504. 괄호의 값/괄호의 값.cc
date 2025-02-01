#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool is_number(const string& s) {
    for (char c : s) {
        if (!isdigit(c)) return false;
    }
    return true;
}

int main() {
    string s;
    cin >> s;

    vector<string> stack;
    for (const char& c : s) {
        if (c == '(' || c == '[') {
            stack.push_back(string(1, c));
        } else {
            if (c == ')') {
                if (stack.empty() || stack.back() == "[" || stack.back() == "]") {
                    cout << "0" << endl;
                    return 0;
                } else {
                    int sum = 0;

                    while (!stack.empty() && stack.back() != "(") {
                        if (stack.back() == "[" || stack.back() == "]" || stack.back() == ")") {
                            cout << "0" << endl;
                            return 0;
                        } else {
                            sum += stoi(stack.back());
                            stack.pop_back();
                        }
                    }
                    if (stack.empty()) {
                        cout << "0" << endl;
                        return 0;
                    }

                    stack.pop_back();
                    stack.push_back(to_string(2 * (sum ? sum : 1)));
                }
            } else if (c == ']') {
                if (stack.empty() || stack.back() == "(" || stack.back() == "]") {
                    cout << "0" << endl;
                    return 0;
                } else {
                    int sum = 0;

                    while (!stack.empty() && stack.back() != "[") {
                        if (stack.back() == "(" || stack.back() == ")" || stack.back() == "]") {
                            cout << "0" << endl;
                            return 0;
                        } else {
                            sum += stoi(stack.back());
                            stack.pop_back();
                        }
                    }

                    if (stack.empty()) {
                        cout << "0" << endl;
                        return 0;
                    }

                    stack.pop_back();
                    stack.push_back(to_string(3 * (sum ? sum : 1)));
                }
            }
        }
    }


    int total = 0;

    for (const string& s : stack) {
        if (!is_number(s)) {
            cout << "0" << endl;
            return 0;
        }

        total += stoi(s);
    }

    cout << total << endl;
    return 0;
}
