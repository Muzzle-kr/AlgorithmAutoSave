#include <iostream>
#include <vector>
using namespace std;

int answer = 0;

int calculate_arr(vector<int> arr) {
    int total = 0;

    for (int i = 1; i < arr.size(); i++) {
        total += abs((arr[i - 1] - arr[i]));
    }

    return total;
}

void bt(vector<int>& matrix, vector<bool> & visited, vector<int> & arr) {
    if (arr.size() == visited.size()) {
        answer = max(answer, calculate_arr(arr));
    }

    for (int i = 0; i < visited.size(); i++) {
        if (!visited[i]) {
            visited[i] = true;
            arr.push_back(matrix[i]);
            bt(matrix, visited, arr);
            arr.pop_back();
            visited[i] = false;
        }
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    vector<bool> visited(n, false);

    for (int i = 0; i < n; i++) {
        vector<int> a;
        visited[i] = true;
        a.push_back(v[i]);
        bt(v, visited, a);
        a.pop_back();
        visited[i] = false;
    }

    cout << answer << endl;
    return 0;
}