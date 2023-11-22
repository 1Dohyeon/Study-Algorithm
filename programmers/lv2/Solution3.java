package whatever.programmers.lv2;

import java.util.Stack;

public class Solution3 {

    boolean solution(String s) {
        boolean answer = true;
        String[] parenthesis = s.split("");
        Stack<String> stack = new Stack<>();

        for (String str : parenthesis) {
            if (str.equals("(")) {
                stack.push(str);
            } else {
                if (stack.isEmpty()) {
                    answer = false;
                    break;
                }
                stack.pop();
            }
        }

        if (!stack.isEmpty()) {
            answer = false;
        }

        return answer;
    }
}
