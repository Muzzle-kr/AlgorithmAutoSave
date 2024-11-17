#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

bool isDigit(const string& str) {
    return !str.empty() && all_of(str.begin(), str.end(), ::isdigit);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    unordered_map<string, int> poketmonMapNameIndex;
    unordered_map<int, string> poketmonMapIndexName;
    int n, m;
    
    cin >> n >> m;
    
    for (int i = 1; i <= n; i++) {
        string name;
        cin >> name;
        poketmonMapNameIndex[name] = i;
        poketmonMapIndexName[i] = name;
    }
    
    for (int i = 0; i < m; i++) {
        string question;
        cin >> question;
        
        if (isDigit(question)) {
            cout << poketmonMapIndexName[stoi(question)] << "\n";
        } else {
            auto it = poketmonMapNameIndex.find(question);
            if (it != poketmonMapNameIndex.end()) {
                cout << it->second << "\n";
            }
        }
    }
    return 0;
}
