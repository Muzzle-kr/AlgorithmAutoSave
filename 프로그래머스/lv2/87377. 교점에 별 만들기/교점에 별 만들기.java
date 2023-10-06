import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        int maxValue = 2147000000;
        int minValue = 2147000000;
        String[] answer = {};
        List<long[]> answerList = new ArrayList<>();
        int length = line.length;

        long minX = Long.MAX_VALUE;
        long maxX = Long.MIN_VALUE;
        long minY = Long.MAX_VALUE;
        long maxY = Long.MIN_VALUE;

        for (int i = 0; i < length - 1; i++) {
            for (int j = i + 1; j < length; j++) {
                long a = line[i][0];
                long b = line[i][1];
                long e = line[i][2];
                long c = line[j][0];
                long d = line[j][1];
                long f = line[j][2];

                long mod = a * d - b * c;

                if (mod == 0) continue;

                double xNum = b * f - e * d;
                double yNum = e * c - a * f;
                
                double x = xNum / mod;
                double y = yNum / mod;
                
                if (Math.ceil(x) == x && Math.ceil(y) == y) {
                    answerList.add(new long[] {(long) x, (long) y});
                    minX = Math.min(minX, (long) x);
                    maxX = Math.max(maxX, (long) x);
                    minY = Math.min(minY, (long) y);
                    maxY = Math.max(maxY, (long) y);
                }
            }
        }

        boolean[][] answerTemp = new boolean[(int) (maxY - minY + 1)][(int) (maxX - minX + 1)];
        
        for (long[] ints: answerList) {
            int x = (int) (ints[0] - minX);
            int y = (int) (ints[1] - maxY);
            
            answerTemp[Math.abs(y)][Math.abs(x)] = true;
        }
        
        answer = new String[answerTemp.length];
        
        int i = 0;
        
        for (boolean[] bs : answerTemp) {
            StringBuilder sb = new StringBuilder();
            
            for (boolean b : bs) {
                if (b) {
                    sb.append("*");
                } else {
                    sb.append(".");
                }
            }
            
            answer[i] = sb.toString();
            i++;
        }
        return answer;
    }
}
