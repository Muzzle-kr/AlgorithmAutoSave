#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, team, individual;
    cin >> n >> team >> individual;
    vector<int> ratings;
    int answer = 0;

    for (int i = 1; i <= n; i++) {
        int x, y, z;
        cin >> x >> y >> z;

        int total = x + y + z;
        if (x >= individual && y >= individual && z >= individual && total >= team) {
            answer++;
            ratings.push_back(x);
            ratings.push_back(y);
            ratings.push_back(z);
        }

    }

    cout << answer << endl;
    for (int i = 0; i < ratings.size(); i++) {
        cout << ratings[i] << " ";
    }

    return 0;
}