import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int N;
    static char[] signOfInequality;
    static long maxVal = 0;
    static long minVal = Long.MAX_VALUE;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        signOfInequality = br.readLine().replaceAll("\\s+","").toCharArray();

        for (int i = 0; i < 10; i++) {
            dfs(0, i, new boolean[10], "" + i);
        }

        System.out.println(String.format("%0" + (N + 1) + "d", maxVal));
        System.out.println(String.format("%0" + (N + 1) + "d", minVal));
    }

    static void dfs(int index, int lastValue, boolean[] visited, String number) {
        if (index == N) {
            long num = Long.parseLong(number);
            maxVal = Math.max(maxVal, num);
            minVal = Math.min(minVal, num);
            return;
        }

        char sign = signOfInequality[index];
        visited[lastValue] = true;

        if (sign == '<') {
            for (int currentValue = lastValue + 1; currentValue < 10; currentValue++) {
                if (!visited[currentValue]) {
                    dfs(index + 1, currentValue, visited, number + currentValue);
                }
            }
        } else if (sign == '>') {
            for (int currentValue = 0; currentValue < lastValue; currentValue++) {
                if (!visited[currentValue]) {
                    dfs(index + 1, currentValue, visited, number + currentValue);
                }
            }
        }
        visited[lastValue] = false;
    }
}
