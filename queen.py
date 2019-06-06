out_range= ''
r_row=r_column=mov=fil=col=0

def create_board(n):

    board= [0] * n
    for i in range(n):
        board[i] = [0] * n

    return board


#print(create_board(6))

def out_of_range(board,row, column,):
    #global board
    global out_range
    if row>=len(board) or column>=len(board):
        out_range= "fuera"
    elif row<0 or column<0:
        out_range= "out"
    else:
        out_range= "ok"

def queen_position(board,row, column):
    #global board
    global out_range
    global  r_row
    global  r_column
    out_of_range(board,row - 1, column - 1)
    if out_range== "out":
        print("queen can't be out of board...")
    elif out_range== "ok":
        board[row - 1][column - 1]=2
        r_row= row - 1
        r_column= column - 1

def busy(board,row, column):
    #global board
    if board[row][column]==0:
        return False
    else:
        return True

def obstacle_position(board,row, column):
    #global board
    global out_range
    out_of_range(board,row - 1, column - 1)
    if busy(board,row - 1, column - 1):
        print("an obstacle can't be where there is another object")
        quit()
    else:
        if out_range == "out":
            print("an obstacle can't be out of the board...")
            quit()
        elif out_range == "ok":
            board[row - 1][column - 1] = 1

def movements(board,row, column):
    global out_range
    #global board
    global mov
    vectors=[[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    #movements
    for i in range(0, len(vectors)):
        t_row = row
        t_col = column
        go_ahead=True
        while go_ahead==True:
            count = 0
            t_row+=vectors[i][count]
            count+=1
            t_col+=vectors[i][count]
            out_of_range(board,t_row, t_col)
            if out_range == "fuera":
                go_ahead = False
            else:
                if busy(board,t_row, t_col):
                    go_ahead = False
                else:
                    mov+=1
    print("movements that queen can do:")
    print(mov)

def solver():
    #reading file
    try:
     file_data=open('tt.txt', 'r')
    except:
       print("error opening file...")
       exit()
    #passing file_data to vector and oreganize
    data=file_data.readlines()
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
    queen_position(board,p_queen_row, p_queen_col)
    # checking there aren't obstacles
    if num_obs>=1 or num_obs==0:
      for i in range(2, len(data)):
          total+=1
      if num_obs==total:
            try :
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
            movements(board,r_row, r_column)
      else:
          print("there are more or less obstacles than the document has")
          exit()

solver()
