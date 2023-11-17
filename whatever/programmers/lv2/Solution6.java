package whatever.programmers.lv2;

public class Solution6 {

    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            answer += partitionSum(i, 0, n);
        }
        return answer;
    }

    public int partitionSum(int i, int total, int n) {
        if (total == n) {
            return 1; // 목표숫자 n이 되었을 경우 카운트를 셈
        } else if (total > n) {
            return 0;
        } else {
            return partitionSum(i + 1, total + i, n);
        }
    }

}
