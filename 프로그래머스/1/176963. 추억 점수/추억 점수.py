def solution(name, yearning, photo):
    dic = {}
    answer = []
    for i in range(len(name)):
        dic[name[i]]=yearning[i]
    print(dic)
    for picture in photo:
        score = 0
        for person in picture:
            if person in dic:
                score += dic[person]
        answer.append(score)
    return answer