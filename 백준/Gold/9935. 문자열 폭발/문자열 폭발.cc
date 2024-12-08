#include <iostream>
#include <stack>
#include <queue>

using namespace std;
// 스택의 폭발물의 길이만큼이 같은 지 확인하고 같으면 폭발!

int main() {
    string input, bomb;
    cin >> input >> bomb;

    vector<char> answer;

    for (char c : input) {
        answer.push_back(c);

        if (answer.size() >= bomb.size()) {
            bool match = true;

            for (int i = 0; i < bomb.size(); i++) {
                if (answer[answer.size() - bomb.size() + i] != bomb[i]) {
                    match = false;
                    break;
                }
            }

            if (match) {
                for (int i = 0; i < bomb.size(); i++) {
                    answer.pop_back();
                }
            }
        }
    }

    if (!answer.empty()) {
        for (char c : answer) {
            cout << c;
        }
        cout << endl;
    } else {
        cout << "FRULA" << endl;
    }

    return 0;
}