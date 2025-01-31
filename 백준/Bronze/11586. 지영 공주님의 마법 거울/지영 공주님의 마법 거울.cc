#include <iostream>
#include <vector>

using namespace std;

typedef vector<vector<char>> vvc;

vvc reflect_matrix(vvc& matrix, int state) {
    vvc new_matrix(matrix.size(), vector<char>(matrix.size()));

    if (state == 1) {
        return matrix;
    } else if (state == 2) {
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = matrix.size() - 1; j >= matrix.size() / 2; j--) {
                new_matrix[i][matrix.size() - j - 1] = matrix[i][j];
            }
        }

        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j <= matrix.size() / 2; j++) {
                new_matrix[i][matrix.size() - j - 1] = matrix[i][j];
            }
        }
        return new_matrix;
    } else {
        for (int i = matrix.size() - 1; i >= matrix.size() / 2; i--) {
            for (int j = 0; j < matrix.size(); j++) {
                new_matrix[matrix.size() - i - 1][j] = matrix[i][j];
            }
        }

        for (int i = 0; i <= matrix.size() / 2; i++) {
            for (int j = 0; j < matrix.size(); j++) {
                new_matrix[matrix.size() - i - 1][j] = matrix[i][j];
            }
        }
        return new_matrix;
    }
    return new_matrix;
}

int main() {
    int n;
    cin >> n;

    vector<vector<char>> matrix(n, vector<char>(n));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    
    int state;
    cin >> state;

    matrix = reflect_matrix(matrix, state);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << "";
        }
        cout << endl;
    }

    return 0;
}