import sys

input = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
cnt=0
n=0

while n<=len(input):
    if input[n:n+len(word)]==word:
        cnt+=1
        n+=len(word)
    else:
        n+=1

print(cnt)