#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>

using namespace std;
typedef vector<vector<int>> vvi;

int n, m;
int result = 1e9;

vector<pair<int, int>> houses;
vector<pair<int, int>> chickens;

void combine(const vector<pair<int, int>> & chickens, vector<vector<pair<int, int>>> & combinations, vector<int> combination, int start, int m) {
    if (m == 0) {
        vector<pair<int, int>> combination_pair;

        for (int n : combination) {
            combination_pair.push_back(chickens[n]);
        }

        combinations.push_back(combination_pair);
        return;
    }

    for (size_t i = start; i < chickens.size(); i++) {
        combination.push_back(i);
        combine(chickens, combinations, combination, i + 1, m - 1);
        combination.pop_back();
    }
};

int calculate_minimum_distance(const vector<pair<int, int>> & alive_chickens) {
    int total = 0;

    for (pair<int, int> house_cord : houses) {
        int hx = house_cord.first;
        int hy = house_cord.second;

        int distance = 1e9;

        for (const auto chicken : alive_chickens) {
            int cx = chicken.first;
            int cy = chicken.second;

            distance = min(distance, abs(hx - cx) + abs(hy - cy));
        }

        total += distance;
    }

    return total;
};

int main() {
    cin >> n >> m;
    cin.ignore();

    vvi matrix(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int a;
            cin >> a;

            if (a == 1) {
                houses.push_back({i, j});
            } else if (a == 2) {
                chickens.push_back({i, j});
            }
            matrix[i][j] = a;
        }
    }



    vector<vector<pair<int, int>>> combinations;
    combine(chickens, combinations, {}, 0, m);

    for (const auto combined : combinations) {
        result = min(result ,calculate_minimum_distance(combined));
    }

    cout << result << endl;
    return 0;
}
