/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

import java.util.Arrays;
import java.util.Scanner;

/*
   As the name of the class should be Solution , using Solution.java as the filename is recommended.
   In any case, you can execute your program by running 'java Solution' command.
 */
class Code2 {
    static int Answer;

    static class Ant implements Comparable<Ant> {
        int value;
        int position;

        Ant(int value, int position) {
            this.value = value;
            this.position = position;
        }

        @Override
        public int compareTo(Ant other) {
            return Integer.compare(this.value, other.value);
        }
    }

    public static void main(String args[]) {
        /*
         * The method below means that the program will read from input.txt, instead of
         * standard(keyboard) input.
         * To test your program, you may save input data in input.txt file,
         * and call below method to read from the file when using nextInt() method.
         * You may remove the comment symbols(//) in the below statement and use it.
         * But before submission, you must remove the freopen function or rewrite
         * comment symbols(//).
         */

        /*
         * Make new scanner from standard input System.in, and read data.
         */
        Scanner sc = new Scanner(System.in);
        // Scanner sc = new Scanner(new FileInputStream("input.txt"));

        int T = sc.nextInt();
        for (int test_case = 0; test_case < T; test_case++) {

            Answer = 0;
            /////////////////////////////////////////////////////////////////////////////////////////////
            // 개미의 마리 수
            int N = sc.nextInt();
            int[] positions = new int[N];
            int[] values = new int[N];

            // 개미의 위치 입력
            for (int i = 0; i < N; i++) {
                positions[i] = sc.nextInt();
            }

            // 개미가 들고 있는 값 입력
            for (int i = 0; i < N; i++) {
                values[i] = sc.nextInt();
            }

            // 개미를 value 값에 따라 정렬하기 위해 (value, position) 형태로 배열 생성
            Ant[] ants = new Ant[N];
            for (int i = 0; i < N; i++) {
                ants[i] = new Ant(values[i], positions[i]);
            }
            Arrays.sort(ants); // value 값을 기준으로 개미를 정렬

            // 개미들이 이동하는 거리 합 계산
            for (int i = 0; i < N; i++) {
                // 정렬된 개미의 위치 이동을 계산하여 누적
                Answer += Math.abs(ants[i].position - positions[i]);
            }
            /////////////////////////////////////////////////////////////////////////////////////////////

            // Print the answer to standard output(screen).
            System.out.println("Case #" + (test_case + 1));
            System.out.println(Answer);
        }
        sc.close();
    }
}