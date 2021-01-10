def printBoard(board):
    for line in board:
        print(*list(map(lambda e: e[1] == 2 and " " or (e[1] == 1 and ('\x1b[6;30;42m' + e[0] + '\x1b[0m') or e[0]), line)), sep=" ")
    print("\n")


def solution(m, n, board):
    bm = [[[c, 0] for c in line] for line in board]

    count = 0

    while (True):
        # print("Start", count)
        # printBoard(bm)
        flag = True
        for y in range(m - 1):
            for x in range(n - 1):
                if all(map(lambda state: state != 2, [bm[y][x][1], bm[y][x + 1][1], bm[y + 1][x][1],
                                                      bm[y + 1][x + 1][1]])) and [
                    bm[y][x + 1][0], bm[y + 1][x][0], bm[y + 1][x + 1][0]] == [bm[y][x][0]] * 3:
                    for i in range(4):
                        if bm[y + i // 2][x + i % 2][1] == 0:
                            count += 1
                            flag = False
                    [bm[y][x][1], bm[y][x + 1][1], bm[y + 1][x][1], bm[y + 1][x + 1][1]] = [
                                                                                               1] * 4

        if flag:
            break
        # print("Destroy")
        # printBoard(bm)

        for y in range(m - 1, -1, -1):
            for x in range(n):
                if bm[y][x][1] != 0:
                    for dy in range(y - 1, -1, -1):
                        if bm[dy][x][1] == 0:
                            [bm[y][x][0], bm[y][x][1]] = [bm[dy][x][0], bm[dy][x][1]]
                            bm[dy][x][1] = 2
                            break
                    if bm[y][x][1] != 0:
                        bm[y][x][1] = 2

    return count


if __name__ == "__main__":
    test = ["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE"]
    print(solution(6, 6, test))
