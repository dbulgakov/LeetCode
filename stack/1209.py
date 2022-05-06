class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        counter = [(s[0], 1)]

        for letter in s[1:]:
            if any(counter):
                last_item = counter[-1]
                if last_item[0] == letter:
                    counter[-1] = (last_item[0], last_item[1] + 1)

                    if counter[-1][1] == k:
                        counter.pop()
                else:
                    counter.append((letter, 1))
            else:
                counter.append((letter, 1))

        res = ''

        for letter, count in counter:
            res += letter * count

        return res
