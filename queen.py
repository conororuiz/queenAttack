from collections import Counter

def create_board(n):
    """
    This function create the board

    :param n: This is the size of the board

    :return: A nested list
    """
    board= [0] * n
    for i in range(n):
        board[i] = [0] * n
    return board

def out_of_range(board,row, column):
    """
    To check if the move is out of range

    :param board: Is a nested list

    :param row: Is the position of the row

    :param column: Is the position of the column

    :return: A boolean to check the range of the matrix
    """
    if row>=len(board) or column>=len(board) or row<0 or column<0:
        return True
    return False

def queen_position(board,row, column):
    """
    Assign the queen in a free position of the board

    :param board: Is a nested list

    :param row: Is the position of the row

    :param column: Is the position of the column

    :return: A list with the position of the queen
    """
    if out_of_range(board,row - 1, column - 1):
        print("queen can't be out of board...")
    else:
        board[row - 1][column - 1]=2
        return [row - 1,column - 1]

def busy(board,row, column):
    """
    To verify position of the board is busy

    :param board: Is a nested list

    :param row: Is the position of the row

    :param column: Is the position of the column

    :return: A boolean
    """
    if board[row][column]==0:
        return False
    return True

def obstacle_position(board,row, column):
    """
    This function assign a obstacle in a position of the board

    :param board: Is a nested list

    :param row: Is the position of the row

    :param column: Is the position of the column

    :return: None
    """
    if busy(board,row-1,column-1):
        print("an obstacle can't be where there is another object")
        quit()
    else:
        if out_of_range(board,row - 1, column - 1):
            print("an obstacle can't be out of the board...")
            quit()
        else:
            board[row-1][column-1] = 1

def movements(board,row,column,vector):
    """
    This function loop over the board and assign the number
    five to a free position to move the queen

    :param board: Is a nested list

    :param row: Is the position of the row

    :param column: Is the position of the column

    :param vector: Is a list, that represent a move in the board

    :return: The board with movements in a direction
    """
    new_x = row + vector[0]
    new_y = column + vector[1]
    count_movements = 0
    if out_of_range(board,new_x, new_y) == False and board[new_x][new_y] == 0:
        board[new_x][new_y] = 5
        movements(board , new_x , new_y , vector)
        return board
    else:
        return board


def solver():
    """
    This function do the reading of the file, validate the data
    and pass the clean data to the movements function

    :return: A nested list with the possible movements
    """
    vectors = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    p_queen_col=0
    p_queen_row=0
    size=0
    num_obs=0
    file_data=''
    try:
        file_data=open('tt.txt', 'r')
    except:
        print("error opening file...")
        exit()
    data=file_data.readlines() # Passing file_data to vector and oreganize
    for i in range(0, len(data)):
        data[i]=data[i].split()
    #operating file_data
    try:
        size=int(data[0][0])
        num_obs = int(data[0][1])
        p_queen_row=int(data[1][0])
        p_queen_col=int(data[1][1])
    except:
        print("document dosen't have correct format")
        exit()
    total=0
    board=create_board(size)
    queen=queen_position(board,p_queen_row, p_queen_col)
    # checking there aren't obstacles
    if num_obs>=1 or num_obs==0:
        for i in range(2, len(data)):
          total+=1
        if num_obs==total:
            try:
                for i in range(2, len(data)):
                     cont=0
                     fil=int(data[i][cont])
                     cont+=1
                     col=int(data[i][cont])
                     obstacle_position(board,fil, col)
            except:
              print("document dosen't have correct format")
              exit()
            # checking queen movements
            for vector in vectors:
                table = movements(board,queen[0], queen[1] , vector)
        else:
          print("there are more or less obstacles than the document has")
          exit()

    return table

table = solver()

def counter_movements(board):
    """
    :param board: Is a nested list

    :return: None
    """
    total = 0
    for column in board:
        print(column)
        t = Counter(column).get(5)
        try:
            total = total + t
        except:
            pass
    print(total)


counter_movements(table)
