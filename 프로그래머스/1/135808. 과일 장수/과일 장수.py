# 1~k
# m개 씩
# 가장 낮은 점수 기준
# 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익
# 최저 사과 점수 * 한 상자에 담긴 사과 개수 * 상자의 개수

def solution(k, m, score):
    score=sorted(score,reverse=True)
    answer=0
    for i in range(0,len(score),m):
        if len(score[i:i+m])==m:
            answer += min(score[i:i+m])*m
    return answer