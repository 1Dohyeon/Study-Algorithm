package review.solve_java;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Ja01_10814 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 선언

        int N = sc.nextInt();
        String[][] member = new String[N][2];

        for (int i = 0; i < N; i++) {
            // String으로 2차원 배열을 생성하였기에 nextInt가 아닌 next로 받아준다.
            member[i][0] = sc.next(); // 나이 -> 정렬 기준
            member[i][1] = sc.next(); // 이름
        }

        // Array에 내장된 sort함수, Comparator를 이용하여 String을 비교하여 오름차순 정렬한다.
        // Array의 sort는 안정성 정렬이기 때문에 2차원 배열의 2번째 요소는 입력된 순서로 유지된다.
        Arrays.sort(member, new Comparator<String[]>() {
            // 나이순으로 정렬
            @Override
            public int compare(String[] m1, String[] m2) {
                return Integer.parseInt(m1[0]) - Integer.parseInt(m2[0]);
            }

        });

        for (int i = 0; i < N; i++) {
            System.out.println(member[i][0] + " " + member[i][1]);
        }

        sc.close();
    }
}
