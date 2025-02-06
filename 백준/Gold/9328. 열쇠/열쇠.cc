#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cctype>
using namespace std;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--) {
        int n, m;
        cin >> n >> m;
        
        // 입력 그리드를 패딩 적용하여 n+2 x m+2 크기로 생성
        int padded_n = n + 2, padded_m = m + 2;
        vector<vector<char>> grid(padded_n, vector<char>(padded_m, '.'));
        for (int i = 1; i <= n; i++) {
            string line;
            cin >> line;
            for (int j = 1; j <= m; j++) {
                grid[i][j] = line[j-1];
            }
        }
        
        // 초기 열쇠 입력: "0"이면 열쇠 없음, 아니면 소문자 열쇠들이 주어짐.
        vector<bool> hasKey(26, false);
        string keysInput;
        cin >> keysInput;
        if (keysInput != "0") {
            for (char k : keysInput) {
                hasKey[k - 'a'] = true;
            }
        }
        
        // 각 알파벳(문)에 대해, 아직 열쇠가 없어서 방문하지 못한 문 좌표들을 저장.
        vector<vector<pair<int,int>>> doorWait(26);
        
        // 방문 여부 배열
        vector<vector<bool>> visited(padded_n, vector<bool>(padded_m, false));
        
        int documents = 0;
        queue<pair<int,int>> q;
        // 외부(패딩된 grid의 (0,0) 등)에서 시작
        q.push({0,0});
        visited[0][0] = true;
        
        while(!q.empty()){
            auto [x, y] = q.front();
            q.pop();
            
            for (int dir = 0; dir < 4; dir++){
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                
                // 범위 체크
                if (nx < 0 || nx >= padded_n || ny < 0 || ny >= padded_m)
                    continue;
                if (visited[nx][ny])
                    continue;
                // 벽이면 건너뛰기
                if (grid[nx][ny] == '*')
                    continue;
                
                char cell = grid[nx][ny];
                
                // 문서('$')인 경우
                if (cell == '$') {
                    documents++;
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
                // 열쇠(a~z)인 경우
                else if (islower(cell)) {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                    int keyIdx = cell - 'a';
                    // 만약 새 열쇠라면, 대기 중인 문들을 모두 열기
                    if (!hasKey[keyIdx]) {
                        hasKey[keyIdx] = true;
                        for (auto pos : doorWait[keyIdx]) {
                            if (!visited[pos.first][pos.second]) {
                                visited[pos.first][pos.second] = true;
                                q.push(pos);
                            }
                        }
                        // 대기열 초기화
                        doorWait[keyIdx].clear();
                    }
                }
                // 문(A~Z)인 경우
                else if (isupper(cell)) {
                    int keyIdx = cell - 'A';
                    // 열쇠가 있다면 문을 지나갈 수 있음.
                    if (hasKey[keyIdx]) {
                        visited[nx][ny] = true;
                        q.push({nx, ny});
                    } else {
                        // 아직 열쇠가 없으므로, 해당 좌표를 대기열에 저장
                        doorWait[keyIdx].push_back({nx, ny});
                    }
                }
                // 빈 공간('.')인 경우
                else { // cell == '.' 등
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
        }
        
        cout << documents << "\n";
    }
    
    return 0;
}
