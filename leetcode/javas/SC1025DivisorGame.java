package leetCode.DynamicProgramming;

public class SC1025DivisorGame {
    /**
     * n이 주어졌을 때 n의 약수인 x를 고른다.
     * n-x를 한 숫자가 다음 턴의 새로운 n이 된다.
     * 이 과정을 반복해서 더 이상 제시할 x가 없다면 패배*/
    public boolean divisorGame(int n) {
        // dp[i]는 숫자 i에서 게임을 시작했을 때 Alice가 이길 수 있는지 나타내는 배열
        boolean[] dp = new boolean[n + 1];

        // dp[0], dp[1] 는 기본값 false
        for (int i=2; i<=n; i++) {
            // Alice의 차례에서, 가능한 모든 x에 대해 검사
            for (int x=1; x<i; x++) {
                // 만약 x로 나누어지고 i-x에서 Alice가 졌다면,
                // Bob 또한 질 수밖에 없다 => 둘 다 최선을 다하기 때문.
                // 즉, dp[i-x]가 false 라면 dp[i]는 true 가 될 수밖에 없다.
                if (i % x == 0 && !dp[i-x]) { // dp[i-x]==false ==> !dp[i-x]
                    dp[i] = true;
                    break; // 더 이상 검사할 필요 없음
                }
            }
        }

        return dp[n];
    }
}
