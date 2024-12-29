#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> strings;
    int len = 0;
    for (int i = 0; i < n; i++) {
        string tmp;
        cin >> tmp;
        len = tmp.size();
        strings.push_back(tmp);
    }

    string answer = "";

    for (int i = 0; i < len; i++) {
        bool is_same = true;
        char c = strings[0][i];
        for (int j = 1; j < n; j++) {
            if (c != strings[j][i]) {
                answer += "?";
                is_same = false;
                break;
            }
        }
        if (is_same) {
            answer += c;
        }
    }

    cout << answer << endl;
    return 0;
}