#include <iostream>
#include <vector>


using namespace std;
typedef vector<vector<int>> vvi;
typedef vector<vector<char>> vvc;

int main() {
    int n, m;
    cin >> n >> m;
    cin.ignore();

    vvc cloud_map(n, vector<char>(m));

    for (int i = 0; i < n; i++) {
        string word;
        getline(cin, word);

        for (int j = 0; j < m; j++) {
            cloud_map[i][j] = word[j];
        }
    }

    vvi v(n, vector<int>(m, -1));

    for (int i = 0; i < n; i++) {
        int count = -1;

        for (int j = 0; j < m; j++) {
            if (cloud_map[i][j] == 'c') {
                count = 0;
                v[i][j] = count;
            } else if (count != -1) {
                v[i][j] = ++count;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}
