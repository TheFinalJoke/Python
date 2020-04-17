#!/usr/bin/env python3
from random import randint
from enum import Enum
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
        
    def add_to_board(self, position, game_piece):
        for mapping in board_mapping.name:
            print(mapping)
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
        
def check_win():
    pass   
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
    while True:
        play_board.print_board()
        if player1.turn == True:
            try: 
                position = input('Player1 turn, Choose Square -> ')
                if position not in [var for var in board_mapping.name]:
                    raise Exception('Not a valid Square')
            except Exception as e: 
                print(e)
                continue
            play_board.add_to_board(position, player1.value)
            check_win()
            player1.turn = False 
            player2.turn = True
        else: 
            try: 
                position = input('Player2 turn, Choose Square -> ')
                if position not in [value for value in board_mapping.name]:
                    raise Exception('Not a valid Square')
            except Exception as e: 
                print(e)
                continue
            play_board.add_to_board(position, player2.value)
            check_win() 
            player2.turn = False 
            player1.turn = True
    
if __name__ == '__main__':
    run()