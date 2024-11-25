#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

typedef vector<vector<int>> vvi;
int visited[61][61][61];
const int damage[6][3] = { {1, 3, 9}, {1, 9, 3}, {3, 1, 9}, {3, 9, 1}, {9, 1, 3}, {9, 3, 1} };

struct State {
    int hp1, hp2, hp3, count;
};

int bfs(int hp1, int hp2, int hp3) {
    memset(visited, 0, sizeof(visited)); // visited 배열 초기화

    queue<State> q;
    q.push({hp1, hp2, hp3, 0});
    visited[hp1][hp2][hp3] = 1;

    while (!q.empty()) {
        State s = q.front();
        q.pop();
        int h1 = s.hp1;
        int h2 = s.hp2;
        int h3 = s.hp3;
        int count = s.count;

        if (h1 == 0 && h2 == 0 && h3 == 0) {
            return count;
        }
        for(int p = 0; p < 6; p++) {
            int nh1 = max(0, h1 - damage[p][0]);
            int nh2 = max(0, h2 - damage[p][1]);
            int nh3 = max(0, h3 - damage[p][2]);

            if(!visited[nh1][nh2][nh3]) {
                visited[nh1][nh2][nh3] = 1;
                q.push({nh1, nh2, nh3, count + 1});
            }
        }
    }

    return -1;
}

int main() {
    int n;
    cin >> n;

    vector<int> hp(n);

    for (int i = 0; i < n; i++) {
        cin >> hp[i];
    }

    cout << bfs(hp[0], hp[1], hp[2]) << endl;
    return 0;
}
