#include <iostream>
#include <vector>
#include <string>

using namespace std;
vector<int> days = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

bool does_match_time(int x, int y) {
    return x >= 0 && x < 24 && y >= 0 && y < 60;
}

bool does_match_date(int x, int y) {
    return x > 0 && x <= 12 && y > 0 && y <= days[x];
}
int main() {
    int n;
    cin >> n;
    cin.ignore();

    while (n--) {
        string s;
        getline(cin, s);
        int blank_idx = s.find(' ');

        string x = s.substr(0, blank_idx);
        string y = s.substr(blank_idx + 1);

        int ix = stoi(x);
        int iy = stoi(y);

        bool match_time = does_match_time(ix, iy);
        bool match_date = does_match_date(ix, iy);

        cout << (match_time ? "Yes " : "No ") << (match_date ? "Yes" : "No") << endl;
    }

    return 0;
}