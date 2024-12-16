#include <iostream>
#include <vector>

using namespace std;
int n, m;
vector<int> gemstones;

int check(int division, vector<int> gems) {
    int count = 0;

    for(int i = 0; i < gems.size(); i++) {
        count += gems[i] / division;
        if (gems[i] % division != 0) {
            count++;
        }
    }

    return count <= n;
}
int main() {
    cin >> n >> m;

    int max_gem_count = 0;
    for (int i = 0; i < m; i++) {
        int gem;
        cin >> gem;

        max_gem_count = max(max_gem_count, gem);
        gemstones.push_back(gem);
    }

    sort(gemstones.begin(), gemstones.end());

    int left = 1;
    int right = max_gem_count;
    int answer = 1e9;

    while (left <= right) {
        int jealousy = (left + right) / 2;

        if (check(jealousy, gemstones)) {
            answer = min(answer, jealousy);
            right = jealousy - 1;
        } else {
            left = jealousy + 1;
        }
    }

    cout << answer << endl;
    return 0;
}