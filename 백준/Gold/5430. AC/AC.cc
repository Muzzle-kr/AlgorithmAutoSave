// 1. 지민이가 가지고 있는 막대의 길이를 모두 더한다. 처음에는 64cm 막대 하나만 가지고 있다. 이때, 합이 X보다 크다면, 아래와 같은 과정을 반복한다.
// 1-1. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
// 1-2. 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
// 1-3. 이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다.
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;
int x = 0;
char delimiter = ',';

vector<int> splitToVector(string str, char delimiter) {
    if (str.size() == 0) {
        return vector<int>();
    }

    vector<int> internal;
    size_t s_size = str.size();

    string temp;
    for (char c : str) {
        if (c == delimiter) {
            internal.push_back(stoi(temp));
            temp = "";
            continue;
        }
        temp += c;
    }

    internal.push_back(stoi(temp));

    return internal;
}

int main() {
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        string order;
        cin >> order;

        int n;
        cin >> n;

        string str;
        cin >> str;

        vector<int> numbers = splitToVector(str.substr(1, str.size()-2), delimiter);        
        
        bool is_error = false;
        int reverse_count = 0;

        for (char o : order) {
            if (o == 'R') {
                reverse_count++;
            } else {
                if (numbers.size() == 0) {
                    cout << "error" << endl;
                    is_error = true;
                    break;
                }

                if (reverse_count % 2 == 0) {
                    numbers.erase(numbers.begin());
                } else {
                    numbers.erase(numbers.end() - 1);
                }
            }
        }
        
        if (is_error) {
            continue;
        }

        if (reverse_count % 2 == 1) {
            reverse(numbers.begin(), numbers.end());
        }

        cout << "[";
        for (int i = 0; i < numbers.size(); i++) {
            cout << numbers[i];
            if (i != numbers.size() - 1) {
                cout << ",";
            }
        }
        cout << "]" << endl;
    }
    return 0;
}