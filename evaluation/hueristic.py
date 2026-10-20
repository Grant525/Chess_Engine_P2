"""
Material + hand-written heuristics.

Each heuristic is a stub returning 0 -- fill these in yourself.
Weights let you tune how much each term matters.
"""

import chess

from engine.evaluation.base import Evaluator
from engine.evaluation.material import MaterialEvaluator


class HeuristicEvaluator(Evaluator):

    def __init__(self) -> None:
        self.material = MaterialEvaluator()
        self.weights = {
            "piece_square": 1.0,
            "mobility": 1.0,
            "pawn_structure": 1.0,
            "king_safety": 1.0,
            "center_control": 1.0,
            "bishop_pair": 1.0,
            "rook_files": 1.0,
        }

    def evaluate(self, board: chess.Board) -> int:
        score = self.material.evaluate(board)
        score += self.weights["piece_square"] * self.piece_square_tables(board)
        score += self.weights["mobility"] * self.mobility(board)
        score += self.weights["pawn_structure"] * self.pawn_structure(board)
        score += self.weights["king_safety"] * self.king_safety(board)
        score += self.weights["center_control"] * self.center_control(board)
        score += self.weights["bishop_pair"] * self.bishop_pair(board)
        score += self.weights["rook_files"] * self.rook_files(board)
        return int(score)


    def piece_square_tables(self, board: chess.Board) -> int:
        # TODO: bonus/penalty per piece based on its square (and game phase).
        return 0

    def mobility(self, board: chess.Board) -> int:
        # TODO: reward having more legal/pseudo-legal moves than the opponent.
        return 0

    def pawn_structure(self, board: chess.Board) -> int:
        # TODO: doubled, isolated, backward, passed pawns, pawn chains.
        return 0

    def king_safety(self, board: chess.Board) -> int:
        # TODO: pawn shield, open files near king, attackers near king.
        return 0

    def center_control(self, board: chess.Board) -> int:
        # TODO: occupation/attacks on d4, e4, d5, e5.
        return 0

    def bishop_pair(self, board: chess.Board) -> int:
        # TODO: bonus for keeping both bishops.
        return 0

    def rook_files(self, board: chess.Board) -> int:
        # TODO: rooks on open / semi-open files, rooks on the 7th rank.
        return 0