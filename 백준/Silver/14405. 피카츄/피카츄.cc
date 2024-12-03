#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
string word;

int countSubstring(string str, string subStr) {
    int count = 0;
    size_t nPos = 0;
    while ((nPos = str.find(subStr, nPos)) != string::npos) {
        count++;
        nPos += subStr.size();
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> word;
    int pi_count = countSubstring(word, "pi");
    int ka_count = countSubstring(word, "ka");
    int chu_count = countSubstring(word, "chu");

    if ((pi_count * 2) + (ka_count * 2) + (chu_count * 3) == word.size()) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    return 0;
}