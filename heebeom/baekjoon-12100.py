# 상, 하, 좌, 우
dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(direct:int):
    visited:list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
    next_field:list[list[int]] = [line[:] for line in field]

    # 하향, 우향인 경우 반대로 역방향으로 반복
    if direct in [1, 3]:
        move_range:list[int] = [n for n in range(N - 1, -1, -1)]
    # 상향, 좌향인 경우 정방향으로 반복
    else:
        move_range:list[int] = [n for n in range(N)]

    for y in move_range:
        for x in move_range:
            if field[y][x] > 0:
                # 다른 블록을 만날때까지 블록을 이동
                cy, cx = y, x
                while True:
                    dy, dx = dyx[direct]
                    ny, nx = cy + dy, cx + dx
                    if (not ((0 <= ny < N) and (0 <= nx < N))
                        or (next_field[ny][nx] > 0)):
                        break
                    cy, cx = ny, nx

                # 이동한 블록을 결과 배열에 저장
                next_field[y][x] = 0
                next_field[cy][cx] = field[y][x]
                
                # 이동한 블럭이 합쳐지는지 검사
                ny, nx = cy + dy, cx + dx
                if (0 <= ny < N) and (0 <= nx < N):
                    if ((next_field[cy][cx] == next_field[ny][nx])
                        and not visited[ny][nx]):
                        # 같은 블록 합치기
                        visited[ny][nx] = True
                        next_field[ny][nx] *= 2
                        next_field[cy][cx] = 0

    return next_field, max(map(max, next_field))


def dfs(biggest, depth):
    global field, answer

    if depth == 5:
        answer = max(answer, biggest)
        return

    for direction in range(4):
        field_copy, biggest_copy = [line[:] for line in field], biggest
        field, biggest = move(direction)
        
        dfs(biggest, depth + 1)
        field, biggest = field_copy, biggest_copy


N:int = int(input())
field:list[list[int]] = []
answer:int = -1

for _ in range(N):
    field.append(list(map(int, input().split())))

dfs(0, 0)
print(answer)