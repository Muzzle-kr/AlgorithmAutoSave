#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int answer = 0;

bool is_difference_once(string s1, string s2) {
    int count = 0;

    for (int i = 0; i < s1.size(); i++) {
        if (s1[i] != s2[i]) {
            count++;
        }
    }

    return count == 1;
}

void dfs(string current_string, string target, vector<string> words, vector<bool> & chk, int count) {
    if (current_string == target) {
        answer = count;
        return;
    }

    for (int i = 0; i < words.size(); i++) {
        if (!chk[i] && is_difference_once(current_string, words[i])) {
            chk[i] = true;
            dfs(words[i], target, words, chk, count + 1);
            chk[i] = false;
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    if (find(words.begin(), words.end(), target) == words.end()) {
        return 0;
    }

    vector<bool> chk(words.size(), false);

    dfs(begin, target, words, chk, 0);
    return answer;

}