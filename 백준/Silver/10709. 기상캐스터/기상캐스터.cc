#include <iostream>
#include <vector>


using namespace std;
typedef vector<vector<int>> vvi;
typedef vector<vector<string>> vvs;

int main() {
    int n, m;
    cin >> n >> m;
    cin.ignore();

    vvs cloud_map(n, vector<string>(m));

    for (int i = 0; i < n; i++) {
        string word;
        getline(cin, word);

        for (int j = 0; j < m; j++) {
            cloud_map[i][j] = word[j];
        }
    }

    vvi v(n, vector<int>(m, -1));

    // 구름이
    for (int i = 0; i < n; i++) {
        bool found = false;
        int count = -1;

        for (int j = 0; j < m; j++) {
            if (cloud_map[i][j] == "c") {
                found = true;
                count = 0;
                v[i][j] = count;
            } else {
                if (found) {
                    count++;
                    v[i][j] = count;
                }
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
