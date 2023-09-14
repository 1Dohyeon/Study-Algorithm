package review.solve_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Ja03_10814 {

    private static class Member {
        int age;
        String name;

        public int getAge() {
            return age;
        }

        public String getName() {
            return name;
        }

        public Member(int age, String name) {
            this.age = age;
            this.name = name;
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언

        int N = Integer.parseInt(br.readLine());
        Member[] member = new Member[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            member[i] = new Member(Integer.parseInt(st.nextToken()), st.nextToken());
        }

        Arrays.sort(member, new Comparator<Member>() {
            @Override
            public int compare(Member m1, Member m2) {
                return m1.age - m2.age;
            }

        });

        for (int i = 0; i < N; i++) {
            System.out.println(member[i].getAge() + " " + member[i].getName());
        }
    }
}
