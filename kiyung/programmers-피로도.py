from itertools import permutations

def solution(k, dungeons):
    dungeons_list = list(permutations(dungeons,len(dungeons)))
    answer = -1

    for i in dungeons_list:
        tmp_k = k
        result = 0
        for j in i:
            if tmp_k >= j[0]:
                tmp_k = tmp_k - j[1]
                result = result + 1
        if result > answer : answer = result
        
    return answer