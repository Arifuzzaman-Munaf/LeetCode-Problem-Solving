class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return "1" + word
        comp = ""
        i = 1
        current_c = word[0]
        for c in word[1:]:
            if current_c == c:
                if i == 9:
                    comp += "9" + current_c
                    i = 1
                else:
                    i += 1
            else:
                comp += f"{i}{current_c}"
                current_c = c
                i = 1
        comp += f"{i}{current_c}"
        return comp


print(Solution().compressedString("aaaaaaaaaaaaaabb"))
