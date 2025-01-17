#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;

int main() {


    while (true) {
        vector<int> v(26, 0);
        string s;
        getline(cin, s);

        if (s == "*") {
            break;
        }

        for (char c : s) {
            if (isalpha(c)) { // 알파벳인 경우에만 처리
                int normalized = static_cast<int>(c) - static_cast<int>('a');
                v[normalized] = 1;
            }
        }

        bool found_missing = false;
        for (int i = 0; i < v.size(); ++i) {
            if (!v[i]) {
                cout << "N" << endl;
                found_missing = true;
                break;
            }
        }
        if (!found_missing) {
            cout << "Y" << endl;
        }
    }

    return 0;
}