class Solution:
    def coinChange(self, Array: List[int], Sum: int) -> int:
        N = len(Array)
        DP = []
        for i in range(N + 1):
            List = [0] + [10e5] * (Sum)
            DP.append(List)

        for ArraySize in range(1, N + 1):
            for SumVal in range(1, Sum + 1):
                if Array[ArraySize - 1] <= SumVal:
                    DP[ArraySize][SumVal] = min(1 + DP[ArraySize][SumVal - Array[ArraySize - 1]],
                                                DP[ArraySize - 1][SumVal])
                else:
                    DP[ArraySize][SumVal] = DP[ArraySize - 1][SumVal]
        if DP[N][Sum] == 10e5:
            return -1
        return DP[N][Sum]
