import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        BigInteger[] fibonacci = new BigInteger[n + 1];

        if (n == 0) {
            bw.write("0");
        } else if (n == 1) {
            bw.write("1");
        } else {
            fibonacci[0] = BigInteger.ZERO;
            fibonacci[1] = BigInteger.ONE;
    
            for (int i = 2; i < n+1; i++) {
                fibonacci[i] = fibonacci[i-2].add(fibonacci[i-1]);
            }
            
            bw.write(fibonacci[n].toString());
        }
        bw.newLine();
        br.close();
        bw.close();
    }
}
