class Codec:
    def encode(self, strs: list[str]) -> str:

        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    def decode(self, s: str) -> list[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            # getting the length of the next string
            length = int(s[i:j])

            # extracting the string and adding to result
            string = s[j+1:j+1+length]
            result.append[string]

            i = j + 1 + length
        
        return result