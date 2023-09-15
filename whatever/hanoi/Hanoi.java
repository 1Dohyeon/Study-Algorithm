package hanoi;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Hanoi {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine()); // 원판 개수
        char A = 'A'; // 출발 기둥
        char C = 'C'; // 도착 기둥
        char B = 'B'; // 임시 기둥

        hanoi(n, A, C, B); // A를 출발 기둥, C를 도착 기둥으로 지정
    }

    public static void hanoi(int n, char from, char to, char temp) {
        //                     (원판 갯수, 출발 기둥, 도착 기둥, 임시 기둥)
        if (n == 1) {
            System.out.println("Move Disk 1 " + from + " to " + to);
        } else {
            hanoi(n-1, from, temp, to);
            System.out.println("Move Disk " + n + " " + from + " to " + to);
            hanoi(n-1, temp, to, from);
        }
    }
}
