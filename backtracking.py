from n_queens_problem import *
global count
count = 1
def check(board):
    for i in range(0,len(board)):
        for x in range(i+1,len(board)):
            ###check row##
            if(board[i]==board[x]):
                return False;
            ###check diagonal fields##
            if(board[i]<board[x]):
                if((x-i)+board[i]==board[x]):
                    return False;
            if(board[i]>board[x]):
                if(board[i]-(x-i)==board[x]):
                    return False;
    return True;
    
def backtracking(board,col):
    global count 
    for i in range(0,8):
        new_board = board + [i]
        if(check(new_board)):
            if(len(new_board)==8):
                print(count,". solution: ", new_board)
                count += 1
            else:
                backtracking(new_board,col+1)
        
backtracking([],0)
        
