#include <iostream>
#include <vector>

using namespace std;

int n;
int a, b, c, d;
int answer = 1e9;
vector<int> answer_combination;

void distinguish(int combi, const vector<vector<int>> & matrix) {
    vector<int> total_arr(5, 0);
    vector<int> current_combination;
    for (int i = 0; i < n; i++) {
        if (combi & (1 << i)) {
            current_combination.push_back(i + 1);
            for (int j = 0; j < 5; j++) {
                total_arr[j] += matrix[i][j];
            }
        }
    }

    if (total_arr[0] >= a && total_arr[1] >= b && total_arr[2] >= c && total_arr[3] >= d) {
        if (answer > total_arr[4]) {
            answer = total_arr[4];
            answer_combination = current_combination;
        } else if (answer == total_arr[4] && current_combination < answer_combination) {
            answer_combination = current_combination;
        }
    }
}

int main() {
    cin >> n;
    cin >> a >> b >> c >> d;

    vector<vector<int>> matrix(n, vector<int>(5, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> matrix[i][j];
        }
    }

    for (int i = 1; i < (1 << n); i++) {
        distinguish(i, matrix);
    }

    if (answer == 1e9) {
        cout << "-1" << endl;
    } else {
        cout << answer << endl;
        for (int i : answer_combination) {
                cout << i << " ";
        }
    }
    return 0;
}
