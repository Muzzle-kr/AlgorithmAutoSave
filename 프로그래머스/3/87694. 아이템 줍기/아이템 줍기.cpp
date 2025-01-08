#include <string>
#include <vector>
#include <tuple>
#include <queue>

using namespace std;
typedef vector<vector<int>> vvi;
typedef vector<vector<bool>> vvb;
vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};
int answer = 0;

void bfs(vvi & map, int characterX, int characterY, int itemX, int itemY) {
    vvb visited(102, vector<bool>(102, false));
    deque<tuple<int, int, int>> q;
    q.push_back({characterX, characterY, 0});

    while (!q.empty()) {
        auto [x, y, count] = q.front();
        q.pop_front();

        if (x == itemX && y == itemY) {
            answer = count / 2;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= 102 || ny < 0 || ny >= 102 || visited[nx][ny]) {
                continue;
            }

            if (map[nx][ny] == 1) {
                visited[nx][ny] = true;
                q.push_back({nx, ny, count + 1});
            }
        }
    }
}

void drawRectangle(vvi & map, vvi rectangle) {
    for (auto& r : rectangle) {
        int x1 = r[0] * 2;
        int y1 = r[1] * 2;
        int x2 = r[2] * 2;
        int y2 = r[3] * 2;
        
        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                if (i == x1 || i == x2 || j == y1 || j == y2) {
                    if (map[i][j] == 0) {
                        map[i][j] = 1;
                    }
                } else {
                    map[i][j] = 9;
                }
            }
        }
    }
}

int solution(vvi rectangle, int characterX, int characterY, int itemX, int itemY) {
    vvi map(102, vector<int>(102, 0));
    drawRectangle(map, rectangle);
    bfs(map, characterX * 2, characterY * 2, itemX * 2, itemY * 2);
    return answer;
}