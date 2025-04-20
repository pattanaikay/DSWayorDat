class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(instructions)
        score = 0
        i = 0
        visited = set()

        while 0 <= i < n and i not in visited:
            if i in visited:
                break
            visited.add(i)
            
            if instructions[i] == "add":
                score += values[i]
                i += 1
            else:
                i += values[i]
        
        return score