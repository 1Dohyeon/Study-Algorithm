package whatever.programmers.lv1;

public class Solution1 {
    public int solution(int n) {
        // 1. int -> String
        String str = Integer.toString(n);
        // 2. String 문자를 분리 후 배열에 담음
        String[] nums = str.split("");

        // 3. 배열의 원소를 모두 더해줌
        int answer = 0;
        for (String num : nums) {
            answer += Integer.parseInt(num);
        }

        return answer;
    }
}
