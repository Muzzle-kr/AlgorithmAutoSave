#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;
typedef vector<vector<int>> vvi;

vector<set<int>> combinations;
int answer = 1e9;
int n; 

int calculate_diff(vvi& matrix, set<int>& combination, set<int>& rest) {
    int sum1 = 0;
    vector<int> combi(combination.begin(), combination.end());
    for (int i = 0; i < combi.size(); i++) {
        for (int j = 0; j < combi.size(); j++) {
            sum1 += matrix[combi[i]][combi[j]];
        }
    }

    int sum2 = 0;

    vector<int> rest_v(rest.begin(), rest.end());
    for (int i = 0; i < rest_v.size(); i++) {
        for (int j = 0; j < rest_v.size(); j++) {
            sum2 += matrix[rest_v[i]][rest_v[j]];
        }
    }
    return abs(sum1 - sum2);
}

void make_combination(int idx, int combi_length, set<int>& combination) {
    if (combination.size() == combi_length) {
        combinations.push_back(combination);
        return;
    }

    for (int i = idx + 1; i < n; i++) {
        combination.insert(i);
        make_combination(i, combi_length, combination);
        combination.erase(i);
    }
}

int main() {
    cin >> n;

    vvi matrix(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    set<int> setto;

    for (int i = 0; i < n; i++) {
        setto.insert(i);
    }
    
    set<int> combination;
    size_t combi_length = n / 2;
    make_combination(-1, combi_length, combination);
    
    for (auto combination : combinations) {
        set<int> rest;
        set_difference(
            setto.begin(), setto.end(), 
            combination.begin(), combination.end(), 
            inserter(rest, rest.begin())
        );
        answer = min(answer, calculate_diff(matrix, combination, rest));
    }
    

    cout << answer << endl;
    return 0;

}