package whatever.programmers.lv2;

public class Solution2 {
    public String solution(String s) {
        String answer = "";
        String[] words = s.split(" "); // 공백을 기준으로 문자열 자르기

        // 공백을 기준으로 잘려진 문자열의 수만큼 반복
        for (String w : words) {
            /*
             * 이때 " "를 기준으로 분리하므로 문자열이 2개이상 연속으로 나온 경우,
             * "  " 를 " "을 기준으로 분리하면 "" 가 배열에 들어가게 됨.
             * ("  " = " " + "" + " ")
             */
            if (w.length() == 0) {
                answer += " ";
            } // 단어가 공백일 경우 반환값에 공백 더하기
            else {
                answer += w.substring(0, 1).toUpperCase(); // 단어 첫번째 대문자로 변환
                answer += w.substring(1, w.length()).toLowerCase(); // 첫글자를 제외한 나머지 소문자로 변환
                answer += " "; // 띄어쓰기
            }

        }

        // 원래 문자열 마지막이 공백일 경우 그대로 answer 반환
        if (s.substring(s.length() - 1, s.length()).equals(" ")) {
            return answer;
        }
        // 마지막에 공백이 더해져서 그 공백을 제외한 answer값 반환
        return answer.substring(0, answer.length() - 1);
    }
}
