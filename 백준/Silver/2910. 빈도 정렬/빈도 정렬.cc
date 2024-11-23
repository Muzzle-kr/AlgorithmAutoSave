#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

map<int, int> freq_map;
unordered_map<int, int> first_appearance;

int main() {
    int n, m;
    cin >> n >> m;
    cin.ignore();

    string line;
    getline(cin, line);
    stringstream ss(line);

    int number, index = 0;

    vector<int> numbers;
    while (ss >> number) {
        numbers.push_back(number);

        if (first_appearance.find(number) == first_appearance.end()) {
            first_appearance[number] = index++;
        }
    }

    for (int num : numbers) {
        freq_map[num] += 1;
    }

    vector<pair<int, int>> freq_vector(freq_map.begin(), freq_map.end());

    sort(freq_vector.begin(), freq_vector.end(),
        [&](const pair<int, int> & p1, const pair<int, int> & p2) {
            if (p1.second == p2.second) {
                return first_appearance[p1.first] < first_appearance[p2.first];
            }
            return p1.second > p2.second;
        });

    for (pair<int, int> p : freq_vector) {
        for (int i = 0; i < p.second; i++) {
            cout << p.first << " ";
        }
    }
    return 0;
}