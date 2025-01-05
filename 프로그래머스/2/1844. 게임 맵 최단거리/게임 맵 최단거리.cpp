#include <vector>
#include <queue>
#include <tuple>

using namespace std;
typedef vector<vector<int>> vvi;

vector<int> dx = {0, 0, 1, -1};
vector<int> dy = {1, -1, 0, 0};

int solution(vvi maps)
{
    int answer = -1;
    int n = maps.size();
    int m = maps[0].size();

    vvi visited(n, vector<int>(m, 0));

    deque<tuple<int, int, int>> q;
    q.push_back({0, 0, 1});
    visited[0][0] = 1;

    while (!q.empty()) {
        auto [x, y, count] = q.at(0);
        q.pop_front();

        if (x == n - 1 && y == m - 1) {
            answer = count;
            break;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            if (!visited[nx][ny] && maps[nx][ny] == 1) {
                visited[nx][ny] = 1;
                q.push_back({nx, ny, count + 1});
            }
        }
    }
    return answer;
}