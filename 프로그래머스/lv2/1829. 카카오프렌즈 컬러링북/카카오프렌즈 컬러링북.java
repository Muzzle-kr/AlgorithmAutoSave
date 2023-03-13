import java.util.*;

class Solution {
    public int[] solution(int n, int m, int[][] picture) {
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        int tot = 0;
        int maxTot = 0;

        Queue<int[]> q = new LinkedList<>();

        int[][] visit = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(visit[i], 0);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (picture[i][j] != 0 && visit[i][j] == 0) {
                    visit[i][j] = 1;
                    tot++;
                    int cnt = 1;
                    q.offer(new int[]{i, j});

                    while (!q.isEmpty()) {
                        int[] pos = q.poll();
                        int x = pos[0];
                        int y = pos[1];

                        for (int k = 0; k < 4; k++) {
                            int nx = x + dx[k];
                            int ny = y + dy[k];

                            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                                if (picture[nx][ny] == picture[x][y] && visit[nx][ny] == 0) {
                                    cnt++;
                                    visit[nx][ny] = 1;
                                    q.offer(new int[]{nx, ny});
                                }
                            }
                        }
                    }
                    maxTot = Math.max(maxTot, cnt);
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = tot;
        answer[1] = maxTot;
        return answer;
    }
}