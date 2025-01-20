# n명이 입국심사 줄
# 모든 사람이 심사를 받는데 걸리는 시간 최솟값 return 
# 입국심사를 기다리는 사람 수 n
# 10억 명 이하
# 1분이상 10억분 이하
# 심사관 10만명 이하


def solution(n, times):
    times.sort()
    min_t = times[0]
    max_t = times[-1] * n
    answer = max_t
    
    while min_t <= max_t:
        people = 0
        mid = (min_t+max_t)//2
        for t in times:
            people += mid//t
            if people >=n:
                break
                
        if people >= n:
            answer = mid # 가능하다면 일단 저장
            max_t = mid - 1 # 무한루프에 빠질 수 있기 때문에 mid 값외에 mid+1, mid-1 등을 넣음
        else:
            min_t = mid + 1
            
    return answer