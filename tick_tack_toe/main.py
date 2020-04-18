#!/usr/bin/env python3
from random import randint
from enum import Enum
import pdb
class board_mapping(Enum):
    A1 = 0
    A2 = 2
    A3 = 4
    B1 = 5
    B2 = 7
    B3 = 9
    C1 = 10
    C2 = 12 
    C3 = 14
class Player():

    def __init__(self, value, name):
        self.value = value 
        self.name = name 
        self.turn = False
    def wins(self):
        return f'{name} WINS!!' 
class board():
   
    def __init__(self):
        self.board = ['','|','','|','',
                      '','|','','|','',
                      '','|','','|','']
    def check_if_used(self, position):
            if self.board[position] != '':
                return True
    def add_to_board(self, position, game_piece):
        for placement in board_mapping:
            if placement.name == position:
                if not self.check_if_used(placement.value):
                    self.board[placement.value] = game_piece
                else:
                    print('Position has Been used already')
    def del_to_board(self, position):
        pass
    def print_board(self):
        print('Current Board\n')
        counter = 1 
        for position in self.board:
            if counter % 5 == 0:
               print(f' {position} ')
               if counter != 15:
                   print('-------------')
               counter += 1
            else:
               print(f' {position} ', end='')
               counter += 1
        
def check_win(board_obj):
    possible_wins = [[0,2,4], [5,7,9], [10,12,14],
                    [0,7,14], [4,7,10], [0,5,10],
                    [2,7,12], [4,9,14]]
    for var in possible_wins:
        checking = []
        for index in var:
            if board_obj.board[index] == 'x':
                checking.append(board_obj.board[index])
            elif board_obj.board[index] == 'o':
                checking.append(board_obj.board[index])
            else:
                continue
        if len(checking) < 3:
            continue 
        else:
            if len(set(checking)) == 1:
                return True, checking[0]
            else:
                continue
    return False, ''
def define_players():
    while True:
        try:
            player1_value = input("What does Player1 want x/o --> ")
            if player1_value.lower() not in ['x','o']:
                raise Exception("Incorrect Value, try Again")
            else:
                return Player(player1_value, 'Player1')
        except Exception as e:
            print(e) 
def run():
    print("Welcome to Tick Tac Toe!")
    player1 = define_players()
    if player1.value == 'x':
       print('Player 1 Chose x Player 2 will be o')
       player2 = Player('o', 'Player2')
    else:
        print('Player 1 chose o, Player 2 will be x')
        player2 = Player('x', 'Player2')
        
    play_board = board()
    
    randNum = randint(0,1)
    if randNum == 0:
        player1.turn = True
    else: 
        player2.turn = True
    counter = 0 
    while counter != 9:
        play_board.print_board()
        if player1.turn == True:
            try: 
                position = input('Player1 turn, Choose Square -> ')
                if position not in [board_placing.name for board_placing in board_mapping]:
                    raise Exception('Not a valid Square')
            except Exception as e: 
                print(e)
                continue
            play_board.add_to_board(position, player1.value)
            check_win_var = check_win(play_board)
            if check_win_var[0]:
                if check_win_var[1] == player1.value:
                    play_board.print_board()
                    return 'Player1 Won'
            player1.turn = False 
            player2.turn = True
            counter += 1
        else: 
            try: 
                position = input('Player2 turn, Choose Square -> ')
                if position not in [board_placing.name for board_placing in board_mapping]:
                    raise Exception('Not a valid Square')
            except Exception as e: 
                print(e)
                continue
            play_board.add_to_board(position, player2.value)
            check_win_var = check_win(play_board)
            if check_win_var[0]:
                if check_win_var[1] == player2.value:
                    play_board.print_board()
                    return 'Player 2 won'
            player2.turn = False 
            player1.turn = True
            counter += 1
    print('You ran out of spaces.. Draw')
if __name__ == '__main__':
    print(run())
    