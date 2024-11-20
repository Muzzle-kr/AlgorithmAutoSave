#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>

using namespace std;

typedef vector<tuple<int, int>> vt;
typedef vector<vector<int>> vvi;

vector<vector<tuple<int, int>>> combinations;

void combine(const vector<tuple<int, int>> &empty, vector<tuple<int, int>> &tuples, int start, int r) {
    if (tuples.size() == r) {
        combinations.push_back(tuples);
        return;
    }

    for (int i = start; i < empty.size(); i++) {
        tuples.push_back(empty[i]);
        combine(empty, tuples, i + 1, r);
        tuples.pop_back();
    }
}

// 바이러스를 퍼뜨리는 함수
void spread_virus(vector<vector<int>> &lab, int n, int m) {
    queue<pair<int, int>> q;
    int dy[4] = {-1, 1, 0, 0};
    int dx[4] = {0, 0, -1, 1};

    // 바이러스 위치 큐에 삽입
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (lab[i][j] == 2) {
                q.push({i, j});
            }
        }
    }

    while (!q.empty()) {
        auto [y, x] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            // 맵 범위 확인 및 빈 공간(0)만 전염
            if (ny >= 0 && ny < n && nx >= 0 && nx < m && lab[ny][nx] == 0) {
                lab[ny][nx] = 2;
                q.push({ny, nx});
            }
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    vvi lab(n, vector<int>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> lab[i][j];
        }
    }

    vector<tuple<int, int>> virus;
    vector<tuple<int, int>> empty;

    // 바이러스와 빈 벽 좌표 저장
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (lab[i][j] == 2) {
                virus.push_back(make_tuple(i, j));
            } else if (lab[i][j] == 0) {
                empty.push_back(make_tuple(i, j));
            }
        }
    }

    // 조합 생성
    int r = 3;
    vector<tuple<int, int>> temp;
    combine(empty, temp, 0, r);

    int result = 0;

    // 조합별로 벽을 세운 후 안전 영역 계산
    for (const auto &combination : combinations) {
        vector<vector<int>> new_lab = lab;

        // 벽 세우기
        for (const auto &t : combination) {
            int y = get<0>(t);
            int x = get<1>(t);
            new_lab[y][x] = 1;
        }

        // 바이러스 퍼뜨리기
        spread_virus(new_lab, n, m);

        // 안전 영역 계산
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (new_lab[i][j] == 0) {
                    count++;
                }
            }
        }

        result = max(result, count);
    }

    cout << result << endl;
    return 0;
}
