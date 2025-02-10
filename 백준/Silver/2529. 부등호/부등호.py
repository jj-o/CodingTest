# Backtracking 
# 모든 경우의 수를 탐색하는 과정에서 불필요한 경로를 조기에 차단
# 가능성이 없는 경로는 더 이상 탐색하지 않고 되돌아가는 방법

# 가능성이 없는 경로는 가지치기
# 재귀를 이용하여 상태를 탐색
# 정답이 아닐 경우, 이전 상태로 되돌아가기

n = int(input())
inequality = input().split()
visited = [0] * 10
max_ans = ''
min_ans = ''

def check_condition(a,b,op):
    if op == "<":
        return a<b
    else:
        return a>b
    
def solve(idx,s):
    global max_ans, min_ans
    if idx == (n+1): # 모든 자리를 채웠을 때
        if len(min_ans) == 0: # 아직 최솟값이 저장되지 않았다면
            min_ans = s
        else:
            max_ans = s
        return # return을 해야 런타임 에러가 안 남. 이미 숫자 선택이 끝났는데도 for문이 계속 실해
    
    # s[-1]은 현재까지 만든 수의 가장 마지막 수
    for i in range(10):
        if visited[i] == 0: 
            if idx == 0 or check_condition(s[len(s)-1],str(i),inequality[idx-1]):
                visited[i] = True # 현재 i 숫자를 사용 중임을 표시
                solve(idx+1,s+str(i))
                visited[i] = False

solve(0,'')
print(max_ans)
print(min_ans)