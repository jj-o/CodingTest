# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
# 쇠막대기 자르는 레이저 적어도 하나 존재
# 잘려진 쇠막대기 조각의 총 개수

# 잘려진 조각의 총 개수를 나타내는 정수

question = input()
stack = []
answer = 0

for idx in range(len(question)):
    if question[idx] == '(':
        stack.append('(')
    else:
        stack.pop()
        if question[idx-1] == '(':
            answer += len(stack)
        else:
            answer += 1
            
print(answer)