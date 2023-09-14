package review.solve_java;

import java.util.Scanner;

public class Ja05_codeground_practice001 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int TC;
        int test_case;

        TC = sc.nextInt();

        for (test_case = 1; test_case <= TC; test_case++) {

            int countOfNumber = sc.nextInt();
            int result = 0;

            for (int i = 0; i < countOfNumber; i++) {
                result = result ^ sc.nextInt();
            }

            System.out.println("Case #" + test_case);
            System.out.println(result);
        }

    }
}
