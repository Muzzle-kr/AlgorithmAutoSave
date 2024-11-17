#include <iostream>
#include <map>
#include <tuple>

using namespace std;
int n;

tuple<string, string> split(string s) {
    const char delimter = ' ';
    size_t pos = s.find(delimter);

    string str1 = s.substr(0, pos);
    string str2 = s.substr(pos + 1);
    return make_tuple(str1, str2);
}
int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        int m;
        cin >> m;
        map<string, int> clothes;

        for (int j = 0; j < m; j++) {
            string s;

            cin.ignore();
            getline(cin, s);

            auto [str1, str2] = split(s);
            clothes[str2] += 1;
        }

        int result = 1;

        for (const auto &entry : clothes) {
            result *= (entry.second + 1);
        }

        result -= 1;
        cout << result << endl;
    }
    return 0;
}
