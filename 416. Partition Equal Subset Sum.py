class Solution:
    def canPartition(self, Array: List[int]) -> bool:
        N = len(Array)
        Sum = sum(Array)
        if Sum & 1:
            return False
        else:
            Sum = Sum // 2
            DP = []
            for i in range(N + 1):
                List = [True] + [False] * (Sum)
                DP.append(List)

            for ArraySize in range(1, N + 1):
                for SumVal in range(1, Sum + 1):
                    if Array[ArraySize - 1] <= SumVal:
                        DP[ArraySize][SumVal] = DP[ArraySize - 1 ][SumVal - Array[ArraySize - 1]] or DP[ArraySize - 1 ][SumVal]
                    else:
                        DP[ArraySize][SumVal] = DP[ArraySize - 1 ][SumVal]

            return DP[N][Sum]
    
