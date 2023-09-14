package review.solve_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;

public class Ja02_10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언

        int N = Integer.parseInt(br.readLine());
        String[][] member = new String[N][2];

        for (int i = 0; i < N; i++) {
            // BufferedReader 는 scanner와 달리 한 줄을 읽기에 문자열 분리를 해줘야한다.
            // 번거롭지만 Scanner보다 처리속도가 빨라서 자주 사용한다.
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            member[i][0] = st.nextToken(); // 나이 -> 정렬 기준
            member[i][1] = st.nextToken(); // 이름
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
    }
}
