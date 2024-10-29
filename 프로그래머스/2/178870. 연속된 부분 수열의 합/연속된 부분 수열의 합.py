# 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열
# 부분 수열의 합은 k
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾음
# 길이가 짧은 수열이 여러 개이면 앞쪽에 나오는 수열을 찾는다.

def solution(sequence, k):
    sum = 0
    l = 0
    r = -1
    # print(sequence.index(2))
    answers = []
    
    while True:
        if sum<k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sum == k:
            answers.append([l,r])
    
    answers.sort(key=lambda x:(x[1]-x[0],x[0])) # 길이가 짧은 것부터, 인덱스가 작은 것부터
    return answers[0]