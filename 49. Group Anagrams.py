class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Answer = {}
        for i in strs:
            S = ''.join(sorted(i))
            if S in Answer:
                Answer[S].append(i)
            else:
                Answer[S] = [i]
        return list(Answer.values())
        
