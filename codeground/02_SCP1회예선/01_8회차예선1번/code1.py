'''
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
'''

import sys

'''
	The method below means that the program will read from input.txt, instead of standard(keyboard) input.
	To test your program, you may save input data in input.txt file,
	and call below method to read from the file when using open() method.
	You may remove the comment symbols(#) in the below statement and use it.
	But before submission, you must remove the open function or rewrite comment symbols(#).
'''

#inf = open('input.txt');
inf = sys.stdin

T = inf.readline()

for t in range(0, int(T)):
    
    Answer = 0
    
	#############################################################################################
	#
	#  Implement your algorithm here.
	#  The answer to the case will be stored in variable Answer.
	#
    N = int(inf.readline())  # 개미의 마리 수
    positions = list(map(int, inf.readline().split()))  # 개미의 위치
    values = list(map(int, inf.readline().split()))  # 개미가 들고 있는 값

    
    # 개미를 value 값에 따라 정렬하기 위해 (value, position) 형태로 리스트 생성
    ants = [(values[i], positions[i]) for i in range(N)]
    ants.sort()  # value 값을 기준으로 개미를 정렬

    # 개미들이 이동하는 거리 합 계산
    for i in range(N):
        # 정렬된 개미의 위치 이동을 계산하여 누적
        Answer += abs(ants[i][1] - positions[i])
    #############################################################################################
	
	# Print the answer to standard output(screen).
    print('Case #%d' %(int(t)+1))
    print(Answer)
inf.close()

# 0 1 1 1   0
# 0 1 1 1 0     1
# 0 1 1   0 1   2
# 0 1 1 0   1   1
# 0 1   0 1 1   2
# 0 1 0   1 1   1
# 0   0 1 1 1   2
# 0 0   1 1 1   1

# 총 10번