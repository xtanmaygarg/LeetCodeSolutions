class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        Answer = 0
        A = bin(a)[2 : ]
        B = bin(b)[2 : ]
        C = bin(c)[2 : ]
        Al = len(A)
        Bl = len(B)
        Cl = len(C)
        L = max(Al, Bl, Cl)
        A = '0' * (L - Al) + A
        B = '0' * (L - Bl) + B
        C = '0' * (L - Cl) + C
        for i in range(L):
            if C[i] == '1':
                if A[i] == '0' and B[i] == '0':
                    Answer += 1
            else:
                if A[i] == '1' and B[i] == '1':
                    Answer += 2
                elif A[i] == '1' or B[i] == '1':
                    Answer += 1
        return Answer
