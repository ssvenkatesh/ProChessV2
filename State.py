#!/usr/bin/env python3
import chess
import numpy as np

class State(object):
    def __init__(self,board = None) -> None:
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board

    
    def serialize(self):
        str = self.board.shredder_fen()
        serstate = np.zeros((72))
        piece_values = {"P": 1, "N": 3, "B": 3, "R": 5,"Q": 9, "K": 10,"p": -1, "n": -3, "b": -3, "r": -5, "q": -9, "k": -10}
        
        
        for i in range(64):
            p = self.board.piece_at(i)
            if p is not None:
                serstate[i]=piece_values[p.symbol()]
        
        if self.board.has_queenside_castling_rights(chess.WHITE):
                serstate[0]= serstate[0] + 1
        if self.board.has_queenside_castling_rights(chess.WHITE):
            serstate[7]= serstate[7] + 1
        if self.board.has_queenside_castling_rights(chess.BLACK):
            serstate[56]= serstate[56] + 1
        if self.board.has_queenside_castling_rights(chess.BLACK):
            serstate[63]= serstate[63] + 1

        serstate[65]=(self.board.turn*1.0)
        serstate = serstate.reshape(9,8)

        return serstate

    
    def edges(self):
        return list(self.board.legal_moves)

if __name__ == "__main__":
    s = State()
    print(s.edges())


