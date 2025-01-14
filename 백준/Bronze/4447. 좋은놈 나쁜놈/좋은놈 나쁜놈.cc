#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();
    
    string good = " is GOOD";
    string bad = " is A BADDY";
    string neutral = " is NEUTRAL";

    for (int i = 0; i < n; i++) {
        string s;
        getline(cin, s);

        int count_b = 0, count_g = 0;

        for (char c : s) {
            if (c == 'b' || c == 'B') {
                count_b++;
            } else if (c == 'g' || c == 'G') {
                count_g++;
            }
        }

        if (count_b > count_g) {
            cout << s << bad << endl;
        } else if (count_g > count_b) {
            cout << s << good << endl;
        } else {
            cout << s << neutral << endl;
        }
    }
    return 0;
}