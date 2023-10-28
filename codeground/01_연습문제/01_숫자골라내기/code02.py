'''
You should use the statndard input/output

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

T = inf.readline() # test case

for t in range(0, int(T)):
    
    Answer=0
    
	#############################################################################################
    N = int(inf.readline())	# 1
    
    nums = list(map(int, inf.readline().split()))	# 2
    
    count_map = {}  # 3. 딕셔너리를 사용하여 각 숫자의 출현 횟수를 저장
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1

    for num, count in count_map.items():    # 4
        if count % 2 == 1:
            Answer ^= num
	#############################################################################################
	
	# Print the answer to standard output(screen).
    print('Case #%d' %(int(t)+1))    
    print(Answer)
inf.close()