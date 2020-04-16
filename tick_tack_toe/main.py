#!/usr/bin/env python3
class Player():

    def __init__(self, value, name):
        self.value = value 
        self.name = name
    def wins(self):
        return f'{name} WINS!!' 
class board():
   
    def __init__(self):
        self.board = {'A': ['','|','','|',''],
                      'B': ['','|','','|',''],
                      'C': ['','|','','|','']}
        
    def add_to_board(self, position, value):
        pass

    def del_to_board(self, position):
        pass
    def print_board(self):
        return [value for key, value in self.board.items()]

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
    print(play_board.print_board())
if __name__ == '__main__':
    run()