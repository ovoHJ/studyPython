import tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        #게임판 보여주자
        print(self.ttt)
        #row, col 입력받자

        #check_winner 연 끝내자

if __name__ == '__main__':
    gm = GameManager()
    gm.play()