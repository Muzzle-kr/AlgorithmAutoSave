#include <iostream>
#include <string>
#include <vector>

using namespace std;
string dict = "AEIOU";
int count = 0;
int answer = 0;
bool found = false;

void dfs(int idx, string s, string word) {
    if (found) return;
    count++;
    
    if (word == s) {
        answer = count;
        found = true;
        return;
    }
    
    if (idx == 5) {
        return;
    }
    
    for (int i = 0; i < dict.size(); i++) {
        dfs(idx + 1, s + dict[i], word);
    }
}

int solution(string word) {
    for (int i = 0; i < dict.size(); i++) {
        dfs(1, string(1, dict[i]), word);
        if (found) break;
    }
    
    return answer;
}