class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resulte: list[int] = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                resulte[idx] = i -idx
            stack.append(i)
        return resulte