#!/usr/bin/env python
# coding: utf-8


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[7] + '|' + board[8] + '|' + board[9])   

def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    #player1 = marker
    #if player1 == 'X':
     #   player2 = 'O'
    #else:
        #player2 = 'X'
        
    #return (player1,player2)



def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    #check all rows,columns and diagonals and share all same markers
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random

def choose_first():
    first_player = random.randint(0,1)
    
    if first_player == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def full_board_check(board):
    for full in range(1,10):
        if space_check(board,full):
            return False
    #Board is full if we return true
    return True


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


def replay():
    again = ''
    
    while again != 'Y' and again != 'N':
        again = input('Want to play again (Y/N): ').upper()
    
    if again == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe')

#While loop to keep running the game
while True:
    #Play the game
    
    #set everything up(board, whose first, choose markers)
    the_board = [' ']*10    # empty board
    player1_marker, player2_marker = player_input()  # calling  to player_input to decide the marker(X or O)
    
    turn = choose_first()   #calling choose_first to randomly select player1 or player2
    print(turn + ' will go first.')
    
    play_game = input('Ready to play? (y or n) ')   # asking if they are ready to play
    
    if play_game == 'y':
        game_on = True
    elif play_game == 'n':
        game_on = False
    #game play
    
    while game_on:
        #PLAYER 1 TURN
        if turn == 'Player 1':
            
            #show the board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 2'
        else:
            #PLAYER 2 TURN
            
            #show the board
            display_board(the_board)
            
            #choose a position
            position = player_choice(the_board)
            
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 1'
    
    if not replay():
        break

#Break out of the while loop on replay()






