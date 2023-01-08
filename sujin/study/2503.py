from itertools import permutations
# 모든 세자리의 숫자 조합 리스트
num = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))  
t = int(input())
for _ in range(t):
    q, strlike, ball = map(int, input().split())
    # 모든 경우의 수에서 삭제할 길이를 저장하는 변수
    removed = 0  
    q = list(str(q))

    # 세자리의 숫자 조합 리스트 하나씩 반복
    for i in range(len(num)):
        s, b = 0, 0
        i -= removed
        # 입력받은 숫자를 한자리씩 반복
        for j in range(3):
            q[j] = int(q[j])
            # 사용자의 j번째의 숫자와 num의 i번째 튜플에 있는지 확인
            if q[j] in num[i]:  
                # 있고, 위치도 같으면 스트라이크 횟수 ++
                if j == num[i].index(q[j]):  
                    s += 1
                # 위치는 다르지만 있다면 볼 횟수 ++
                else:  
                    b += 1
        # 사용자의 입력과, 추출해온 결과가 다르다면 후보지에서 제외
        if s != strlike or b != ball:  
            num.remove(num[i])
            # 달라진 리스트 길이를 이해 removed
            removed += 1  
print(len(num))