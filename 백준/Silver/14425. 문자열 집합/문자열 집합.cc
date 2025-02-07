#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    unordered_map<string, int> map;
    int answer = 0;


    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        map.insert({s, 1});
    }

    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;

        if (map.find(s) != map.end()) {
            answer++;
        }
    }

    cout << answer << endl;
}
