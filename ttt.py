import os
import time

class TicTacToe(object):
    """
    standard 2-player, turn-based tic-tac-toe game
    """
    def __init__(self):
        self.markers = ('', 'X', '@')
        self.win_patts = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        self.board_string_patt = '\n| %s | %s | %s |\n| %s | %s | %s |\n| %s | %s | %s |\n'
        return

    def reset_game(self):
        self.board = [0,0,0,0,0,0,0,0,0] #represents the nine squares of board, row-major format
        self.cur_player = 0
        self.winner_pattern = None
        self.available_squares = '012345678'

    def run(self):
        def ask_to_continue():
            ans = raw_input('Would you like to play? (y/n):  ')
            return ans.lower() == 'y'

        while ask_to_continue():
            self.reset_game()
            self.start_game()
        return

    def start_game(self):
        self.draw_board()
        while not self.winner_exists():
            self.cur_player = 1 if (self.cur_player != 1) else 2     
            int_square = self.prompt_move()
            self.process_move(int_square)
            self.draw_board()
        self.print_winner()

    def prompt_move(self):
        while True:
            square = raw_input("player %s, please choose a square: "%(self.cur_player))
            if square in self.available_squares:
                self.available_squares = self.available_squares.replace(square, '')
                int_square = int(square)
                break
            else:
                print 'Invalid Move!!'
        return int_square

    def winner_exists(self):
        for (a,b,c) in self.win_patts:
            if self.board[a] == 0:
                continue
            elif self.board[a] == self.board[b] == self.board[c]:
                self.winner_pattern = (a,b,c)
                return True
        return False

    def process_move(self, square):
        self.board[square] = self.cur_player
        return

    def draw_board(self, markers=None):
        if not markers:
            markers = self.markers
        os.system("clear")
        print self.board_string_patt%tuple(markers[bi] if bi !=0 else i for (i, bi) in enumerate(self.board))
        return

    def print_winner(self):
        """
        with cool flashing animation!!
        """
        tmarkers = list(self.markers)
        for i in range(10):
            if i%2 == 0:
                tmarkers[self.cur_player] = ' '
                self.draw_board(markers=tmarkers)
            else:
                tmarkers[self.cur_player] = self.markers[self.cur_player]
                self.draw_board(markers=tmarkers)
            print 'player %s wins!!!'%self.cur_player
            print '-----------------'
            time.sleep(0.25)
                
        return

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.run()
