class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_clear_text(string: str) -> []:
            res = []
            for letter in string:
                if letter == '#' and len(res) > 0:
                    res.pop()
                elif letter != '#':
                    res.append(letter)
            return res

        return get_clear_text(s) == get_clear_text(t)
