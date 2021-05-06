import copy


def getRotatedBoard(x1, y1, x2, y2, board):
    temp = board[x1][y1]
    minValue = temp
    for i in range(x1, x2):
        board[i][y1] = board[i+1][y1]
        minValue = min(board[i][y1], minValue)
    for i in range(y1, y2):
        board[x2][i] = board[x2][i+1]
        minValue = min(board[x2][i], minValue)
    for i in range(x1, x2+1, -1):
        board[i][y2] = board[i - 1][y2]
        minValue = min(board[i][y2], minValue)
    for i in range(y1, y2 + 1, -1):
        board[x1][i] = board[x1][i - 1]
        minValue = min(board[x1][i], minValue)
    board[x1][y1 + 1] = temp
    return (board, minValue)


def solution(rows, columns, queries):
    board = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(i*rows+j+1)
        board.append(temp)

    answer = []
    for i, query in enumerate(queries):
        x1, y1, x2, y2 = query
        (newBoard, minValue) = getRotatedBoard(
            x1 - 1, y1 - 1, x2 - 1, y2 - 1,  board)
        print(newBoard)
        board = newBoard
        answer.append(minValue)

    return answer
