# 구현문제가 중시
# 최대 5번 이동해서 만들 수 있는 가장 큰 블록
# 상,하,좌,우 * 다섯번
# 순서 중요하니깐 순열
# 4P5
from itertools import product

#빈곳이 없도록 한쪽으로 미는 함수
def move(board, direction):
    #우
    if direction == (1,0):
        for i in range(size):
            arr = list()
            cnt = 0
            for j in range(size):
                if board[i][j] == 0:
                    cnt += 1
                else:
                    arr.append(board[i][j])
            board[i] = [0] * cnt + arr
    #좌
    elif direction == (-1,0):
        for i in range(size):
            arr = list()
            cnt = 0
            for j in range(size):
                if board[i][j] == 0:
                    cnt += 1
                else:
                    arr.append(board[i][j])
            board[i] = arr + [0] * cnt
    #상
    elif direction == (0, 1):
        new_board = [[0] * size for i in range(size)]
        for i in range(size):
            arr = list()
            cnt = 0
            for j in range(size):
                if board[j][i] == 0:
                    cnt += 1
                else:
                    arr.append(board[j][i])
            new_board[i] = arr + [0] * cnt
        board = list(map(list,zip(*new_board)))
    
     #하
    elif direction == (0, -1):
        new_board = [[0] * size for i in range(size)]
        for i in range(size):
            arr = list()
            cnt = 0
            for j in range(size):
                if board[j][i] == 0:
                    cnt += 1
                else:
                    arr.append(board[j][i])
            new_board[i] = [0] * cnt + arr
        board = list(map(list,zip(*new_board)))
    return board


#같은쪽 계산함수
def calculation(board, direction, maxNum):
    #우
    if direction == (1,0):
        stamp = [[False] * size for i in range(size)]
        for i in range(size):
            for j in range(size-2, -1, -1):
                if board[i][j] == board[i][j+1] and not stamp[i][j+1]:

                    stamp[i][j] = True
                    stamp[i-1][j] = True

                    board[i][j+1] += board[i][j]
                    board[i][j] = 0

                    if board[i][j+1] > maxNum:
                        maxNum = board[i][j+1]
                else:
                    continue
    
    #좌
    elif direction == (-1,0):
        stamp = [[False] * size for i in range(size)]
        for i in range(size):
            for j in range(1, size-1, 1):
                if board[i][j] == board[i][j-1] and not stamp[i][j-1]:

                    stamp[i][j] = True
                    stamp[i][j-1] = True

                    board[i][j-1] += board[i][j]
                    board[i][j] = 0

                    if board[i][j-1] > maxNum:
                        maxNum = board[i][j-1]
                else:
                    continue
    

    #상
    elif direction == (0,1):
        stamp = [[False] * size for i in range(size)]
        for i in range(1, size-1, +1):
            for j in range(size):
                if board[i][j] == board[i-1][j]:
                    
                    stamp[i][j] = True
                    stamp[i-1][j] = True

                    board[i-1][j] += board[i][j]
                    board[i][j] = 0

                    if board[i-1][j] > maxNum:
                        maxNum = board[i-1][j]
            
                else:
                    continue
    
    #하
    elif direction == (0,-1):
        stamp = [[False] * size for i in range(size)]
        for i in range(size-2, -1, -1):
            for j in range(size):
                if board[i][j] == board[i+1][j]:
                    
                    stamp[i][j] = True
                    stamp[i+1][j] = True

                    board[i+1][j] += board[i][j]
                    board[i][j] = 0

                    if board[i+1][j] > maxNum:
                        maxNum = board[i-1][j]
                else:
                    continue
    
    return board, maxNum
    
# 한번 방향키마다 작동하는 함수         
def turn(board, direction, maxNum):
    board = move(board, direction)
    board, maxNum = calculation(board,direction, maxNum)
    board = move(board, direction)
    return board, maxNum

    
            

# 상하좌우로 5번 가는 가는 모든 경우의 수 도출
direction = [(1,0), (-1,0), (0,1), (0,-1)]
case = list(product(direction,direction,direction,direction,direction))

#게임판 만들기 
size = int(input())
board = list()
for i in range(size):
    board.append(list(map(int, input().split(" "))))

maxNum = 0
for directions in case:
    test_board = board

    for direction in directions:
        board, maxNum = turn(board, direction, maxNum)

print(maxNum)

                
        
    




    