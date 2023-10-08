public class Solution {
    public static long solution(int cap, int n, int[] deliveries, int[] pickups) {
        int[][] space = new int[n + 1][2];
        int startD = cap, startP = cap;
        long distance = 0;
        int count = 0;

        for (int i = n - 1; i >= 0; i--) {
            int nowD = deliveries[i];
            int nowP = pickups[i];
            space[i][0] = space[i + 1][0] - nowD;
            space[i][1] = space[i + 1][1] - nowP;

            if (space[i][0] < 0 || space[i][1] < 0) {
                int goBack = (i + 1) * 2;

                while (true) {
                    if (space[i][0] >= 0 && space[i][1] >= 0) {
                        break;
                    }
                    space[i][0] += cap;
                    space[i][1] += cap;
                    count++;
                }

                distance += goBack * count;
                count = 0;
            }
        }

        return distance;
    }
}
