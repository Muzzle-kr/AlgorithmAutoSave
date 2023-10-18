import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int E = scanner.nextInt();
        int S = scanner.nextInt();
        int M = scanner.nextInt();
        scanner.close();

        int ee = 1, ss = 1, mm = 1;
        int year = 1;

        for (int i = 0; i < 1000000000; i++) {
            if (ee == E && ss == S && mm == M) {
                System.out.println(year);
                break;
            }

            ee += 1;
            if (ee > 15) {
                ee = 1;
            }

            ss += 1;
            if (ss > 28) {
                ss = 1;
            }

            mm += 1;
            if (mm > 19) {
                mm = 1;
            }

            year += 1;
        }
    }
}