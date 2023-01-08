def permutations(arr:list[int], d:int):
    for i in range(len(arr)):
        if d == 1:
            yield [arr[i]]
        else:
            for next in permutations(arr[:i] + arr[i+1:], d-1):
                yield [arr[i]] + next


def grading_answer(submit:list[int], answer:list[int]):
    strike:int = 0
    ball:int = 0

    for i in range(3):
        if submit[i] == answer[i]:
            strike += 1
        elif submit[i] in answer:
            ball += 1

    return (strike, ball)


def solution(questions: list[list[int], int, int]):
    answers:int = 0
    num_range:list[int] = [i for i in range(1, 10)]
    
    # [1, 2, 3] ~ [9, 8, 7] 까지 모든 경우의 수 실행
    for answer in permutations(num_range, 3):
        # 질문 리스트 순회하기
        for i in range(QUESTION_NUM):
            # 만약 경우의 수가 질문 결과랑 틀리다면 break
            submit, strike, ball = questions[i]
            if grading_answer(submit, answer) != (strike, ball):
                break
            # 전부 일치한다면 정답의 수
            if (i + 1) == QUESTION_NUM:
                answers += 1
                
    print(answers)


N: int = int(input())
questions:list[list[int], int, int] = []

for _ in range(N):
    I, S, B = map(int, input().split())
    questions.append((list(map(int, str(I))), S, B))

QUESTION_NUM:int = len(questions)

solution(questions)