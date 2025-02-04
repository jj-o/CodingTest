n = int(input())
skills = input()

stack_LR = []
stack_SK = []
count = 0

for s in skills:
    if s.isdigit():
        count += 1
    elif s == 'S':
        stack_SK.append(s)
    elif s == 'K':
        if stack_SK: # stack_SK에는 S만 담음음
            stack_SK.pop()
            count += 1
        else:
            break
    elif s == 'L':
        stack_LR.append(s)
    elif s == 'R':
        if stack_LR:
            stack_LR.pop()
            count += 1
        else:
            break

print(count)