from itertools import permutations
n = int(input())


li = list(permutations(['1','2','3','4','5','6','7','8','9'], 3)) # 숫자 조합 생성

for i in range(n):
    answer, s, b =  map(int, input().split())
    answer = [str(answer)[0],str(answer)[1],str(answer)[2]] # str 타입 변환
    c = 0
    for j in range(len(li)): 
        strike = 0
        ball = 0
        j -= c 
        for k in range(3): #
            if li[j][k] == answer[k]: strike += 1
            elif answer[k] in li[j]: ball += 1

        if (strike != s ) or (ball != b): # strike나 ball의 수가 맞지 않을 때는 해당 수를 제거
            li.remove(li[j])
            c += 1
    
print(len(li))