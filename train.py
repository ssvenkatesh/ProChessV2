import chess.pgn
import os
from State import State

def get_dataset(num_games):
    gn=1
    x,y =[],[]
    for gfile in os.listdir("Data"):
        pgn = open(os.path.join("Data",gfile))
        while True:
            try:
                if gn > num_games:
                    return x,y
                game = chess.pgn.read_game(pgn)
                print(num_games,gn,". parsing game.. size:",len(x) , "Title:",game.headers["Event"] )
                gn = gn+ 1
                board = game.board()
                value = {'1/2-1/2':50, '1-0':100, '0-1':-100 } [game.headers['Result']]
                for move in game.mainline_moves():
                    board.push(move)
                    state = State(board).serialize()
                    x.append(state)
                    y.append(0)
                y[-1]=value
            except Exception as e: 
                print({e})
                break
        return x,y
    

if __name__=="__main__":
    get_dataset(10)
    
