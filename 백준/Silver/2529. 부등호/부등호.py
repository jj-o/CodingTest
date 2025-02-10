# 순열 등으로 풀려고 하면 O(n!)
# 경우의 수를 가지치기 해야함

# 9
# > < < < > > > < <

n = int(input())
opers = input().split()
visited = [False] * 10 # 숫자를 방문했는지 확인

def comparison(a,b,oper):
    if oper == '<':
        return a<b # a<b 비교연산이 맞아야 True
    else:
        return a>b

def solve(idx, string_numbers):
    global min_result, max_result
    if idx == (n+1): # 마지막 수까지 사용
        if len(min_result) == 0: # min_result에 저장된 값이 없으면
            min_result = string_numbers
        else:
            max_result = string_numbers
        return
    
    for i in range(10): # 작은 수부터 큰 수 순으로 부등호를 만족하는지 확인 
        if visited[i] == False:
            if idx == 0 or comparison(string_numbers[len(string_numbers)-1],str(i),opers[idx-1]):
                visited[i] = True
                solve(idx+1, string_numbers+str(i))
                visited[i] = False # 재귀호출이 끝나면 다시 visited[i] = False로 하여 다른 경우의 수도 처리


min_result, max_result= '',''
solve(0,'')
print(max_result)
print(min_result)

