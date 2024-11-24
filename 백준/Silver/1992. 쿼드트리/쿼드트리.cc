#include <iostream>
#include <vector>

using namespace std;
typedef vector<vector<int>> vvi;
string answer = "";

void divide(const vvi & v) {
    int length = v.size();
    int mark = v[0][0];

    if (length == 1) {
        answer += to_string(mark);
        return;
    }

    bool canComp = true;

    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            if (mark != v[i][j]) {
                canComp = false;
                break;
            }
        }

        if (!canComp) {
            break;
        }
    }

    if (canComp) {
        answer += to_string(mark);
        return;
    }

    answer += "(";
    int half = length / 2;

    vvi topLeft(half, vector<int>(half));
    for (int i = 0; i < half; i++) {
        for (int j = 0; j < half; j++) {
            topLeft[i][j] = v[i][j];
        }
    }
    divide(topLeft);

    vvi topRight(half, vector<int>(half));
    for (int i = 0; i < half; i++) {
        for (int j = half; j < length; j++) {
            topRight[i][j - half] = v[i][j];
        }
    }
    divide(topRight);

    vvi bottomLeft(half, vector<int>(half));
    for (int i = half; i < length; i++) {
        for (int j = 0; j < half; j++) {
            bottomLeft[i - half][j] = v[i][j];
        }
    }
    divide(bottomLeft);

    vvi bottomRight(half, vector<int>(half));
    for (int i = half; i < length; i++) {
        for (int j = half; j < length; j++) {
            bottomRight[i - half][j - half] = v[i][j];
        }
    }
    divide(bottomRight);
    answer += ")";
};

int main() {
    int n;
    cin >> n;
    cin.ignore();

    vvi matrix(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        for (int j = 0; j < line.size(); j++) {
            matrix[i][j] = line[j] - '0';
        }
    }

    divide(matrix);
    cout << answer << endl;
    return 0;
}
