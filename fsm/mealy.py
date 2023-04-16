# """
# Implementation of a Transition-Assigned Finite State 
# Machine (Mealy Automaton)
# """
# class TSAFM:
#     """
#     where:
#     Q - Set of states
#     S - input alphabet
#     R - output alphabet
#     f - state transition function (Q x S -> Q)
#     g - output function (Q x S -> R)
#     qi - initial state
#     """
#     def __init__(self, Q, S, R, f, g, qi):
#         self.Q = Q
#         self.S = S
#         self.R = R
#         self.f = f
#         self.g = g
#         self.qi = qi

#     def run(self, str):
#         q = self.qi
#         str = str.split(" ")[::-1]
#         while str:
#             print(str.pop())
#             # Reimplement
#             # q = self.delta[(q, str.pop())]
#         return []