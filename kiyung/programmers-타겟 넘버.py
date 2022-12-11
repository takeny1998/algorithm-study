from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    
    q.append([numbers[0],0]) # 첫 번째 +원소 집어넣음
    q.append([-1*numbers[0],0]) # 첫 번째 -원소 집어넣음
    
    # print("pop 전의 q :",q)
    while q:
        temp, index = q.popleft() # temp에 맨 앞 값 저장하고 빼기
        index += 1 # 인덱스 한칸씩 뒤로 밀기
        # print('temp :',temp, 'index :', index)
        # print(q)
        if index < len(numbers): 
            q.append([temp+numbers[index], index]) # temp + numbers[1] (1) = 5, index = 1
            # print(temp+numbers[index])
            q.append([temp-numbers[index], index]) # temp - numbers[1] (-1) = 3, index =1
            # print(temp-numbers[index])
        else:
            if temp == target: # pop한 temp가 마지막 원소이고, target과 같다면 answer += 1
                answer += 1
        # print('temp :',temp)
        # print(q)

    # print("pop 후의 q :",q)
    # print("temp :",temp)
    # print("idx :",idx)
    return answer

print(solution([1,1,1,1,1], 3))
print(solution([4,1,2,1], 4))