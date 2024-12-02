#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int n, k;
int answer = 0;
void find_words(bitset<26> & binary, vector<string> words) {
    int count = 0;

    for (string word : words) {
        bool is_possible = true;
        
        for (char c : word) {
            if (!binary[c - 'a']) {
                is_possible = false;
                break;
            }
        }
        if (is_possible) {
            count++;
        }
    }

    answer = max(answer, count);
}


void dfs(bitset<26> & binary, vector<string> words, int start, int depth) {
    if (depth == k - 5) {
        find_words(binary, words);
        return;
    }

    for (int i = start + 1; i < 26; i++) {
        if (!binary[i] == 1) {
            binary[i] = 1;
            dfs(binary, words, i, depth + 1);
            binary[i] = 0;
        }
    }
}

int main() {
    cin >> n >> k;
    vector<string> words;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        words.push_back(s);
    }

    if (k < 5) {
        cout << 0 << endl;
        return 0;
    }

    if (k == 26) {
        cout << n << endl;
        return 0;
    }

    // a, n, t, i, c 는 무조건 배워야 함
    vector<char> initial_char = {'a', 'n', 't', 'i', 'c'};
    bitset<26> binary;
    binary['a' - 'a'] = 1;
    binary['n' - 'a'] = 1;
    binary['t' - 'a'] = 1;
    binary['i' - 'a'] = 1;
    binary['c' - 'a'] = 1;


    
    dfs(binary, words, -1, 0);

    cout << answer << endl;
    return 0;
}