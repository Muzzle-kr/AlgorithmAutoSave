#include <iostream>
#include <vector>

using namespace std;
int n;
string MAX_ANSWER = "0";
string MIN_ANSWER = "9999999999";

void dfs(string current, int count, vector<char> & signs, vector<int> & visited) {
    if (count == n) {
        MAX_ANSWER = max(MAX_ANSWER, current);
        MIN_ANSWER = min(MIN_ANSWER, current);
        return;
    }

    for (int i = 0; i < 10; i++) {
        if (visited[i]) continue;

        int length = current.size();
        int last_digit = current[length - 1] - '0';

        if (signs[count] == '>') {
            if (last_digit > i) {
                visited[i] = 1;
                dfs(current + to_string(i), count + 1, signs, visited);
                visited[i] = 0;
            }
        } else {
            if (last_digit < i) {
                visited[i] = 1;
                dfs(current + to_string(i), count + 1, signs, visited);
                visited[i] = 0;
            }
        }


    }
}

int main() {
    cin >> n;
    vector<char> signs;

    for (int i = 0; i < n; i++) {
        char c;
        cin >> c;
        signs.push_back(c);
    }


    vector<int> visited(10, 0);

    for (int i = 0; i < 10; i++) {
        visited[i] = 1;
        dfs(to_string(i), 0, signs, visited);
        visited[i] = 0;
    }


    cout << MAX_ANSWER << endl;
    cout << MIN_ANSWER << endl;

    return 0;
}
