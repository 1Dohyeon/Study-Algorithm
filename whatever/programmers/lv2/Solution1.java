package whatever.programmers.lv2;

import java.util.Arrays;

public class Solution1 {

    public String solution(String s) {
        String answer = "";

        String[] nums = s.split(" ");
        int[] numbers = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            numbers[i] = Integer.parseInt(nums[i]);
        }

        Arrays.sort(numbers);
        String max = Integer.toString(numbers[numbers.length - 1]);
        String min = Integer.toString(numbers[0]);

        answer = min + " " + max;
        return answer;
    }
}
