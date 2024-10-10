def solution(numbers):
    answer = []
    stack = []
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]]<numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer