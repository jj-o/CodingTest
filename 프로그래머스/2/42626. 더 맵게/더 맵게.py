# 스코빌 지수를 K이상
# 스코빌 지수 계산
# 모든 음식의 스코빌 지수가 K이상

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        mix = a + 2*b
        answer += 1
        heapq.heappush(scoville,mix)
    return answer