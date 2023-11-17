package whatever.programmers.lv2;

public class Solution5 {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2]; // 빈 배열
        int sum = brown + yellow;

        for (int i = 3; i < sum; i++) { // i = 세로
            int j = sum / i; // j = 가로
            int width = Math.max(i, j); // 가로 > 세로 이므로 최댓값
            int length = Math.min(i, j);

            int center = (width - 2) * (length - 2);

            if (center == yellow) {
                answer[0] = width;
                answer[1] = length;
            }
        }

        return answer;
    }
}
