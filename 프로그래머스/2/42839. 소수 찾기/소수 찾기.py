# 한자리 숫자가 적힌 종이 조각
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return
# 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수
# 경우의 수가 100만 이하이면 완전탐색을 생각해볼 수 있다

import math
from itertools import permutations

def isPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,int(math.sqrt(x)+1)):
            if x%i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    
    # 모든 길이의 숫자의 조합에 대하여 생각해야함
    
    num_set = set() # set와 {} (딕셔너리)는 다름
    
    for i in range(1,len(numbers)+1):
        for perm in permutations(numbers,i):
            num_set.add(int(''.join(perm))) # set에 문자열 대신 정수로 저장 가능!
                        
    for num in num_set:
        if isPrime(num):
            answer +=1
    return answer