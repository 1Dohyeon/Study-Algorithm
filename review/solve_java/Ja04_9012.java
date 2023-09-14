package review.solve_java;

import java.io.*;
import java.util.Stack;

public class Ja04_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < t; i++) {
            String input = br.readLine(); // 괄호
            int length = input.length(); // 괄호 갯수

            for (int j = 0; j < length; j++) {
                char ch = input.charAt(j);

                if (ch == '(') {
                    stack.push(ch);
                } else {
                    // 스택이 비어있는데 ')' 가 들어올 경우 잘못된 괄호이므로 NO 출력을 위해 스택에 push 후 break
                    // 스택이 비어있지 않으면, 스택 pop
                    int size = stack.size();
                    if (size == 0) {
                        stack.push(ch);
                        break;
                    } else {
                        stack.pop();
                    }
                }
            }
            // 스택이 비어있으면 YES, 아니면 NO
            if (stack.isEmpty()) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

            stack.clear();
        }
    }
}
