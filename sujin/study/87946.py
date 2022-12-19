# programmers 피로도
# 피로도 사용 -> 던전탐험
# 최소 필요 피로도, 소모 피로도
# 유저의 현재 피로도 k, 각던전별 최소 필요 피로도, 소모피로도
# 유저가 탐험할 수 있는 최대 던전 수를 return

#1~8이하 완전탐색 가능

from itertools import permutations

def solution(k, dungeons):
    # 던전의 수가 1이상 8이하이므로 완전탐색을 하기에 무리가 없는 문제
    permute = list(permutations(dungeons,len(dungeons)))
    
    #최대값 변수 선언
    max = 0

    # 던전에 순서에 대한 모든 경우의 수를 반복문 돌림
    for i in permute:
        # 몇개의 던전을 갔는지 개수를 세는 변수
        cnt = 0
        # 누적되지 않도록 피로도 리셋
        l = k
        # 던전의 개수만큼 반복
        for j in range(len(i)):
            # 종료 조건: 만약 피로도가 부족하여 던전을 탐색하지 못할 경우
            if l<i[j][0]:
                break
            # 던전의 소모 피로도 빼주기
            l -= i[j][1]
            # 탐색한 던전 수 증가
            cnt += 1

        # 최대로 탐색한 던전 수 업데이트
        if cnt > max:
            max = cnt
    return max

k = 80
dungeons = [[80,20],[50,40],[30,10]]
solution(k, dungeons)