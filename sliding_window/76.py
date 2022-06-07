from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def delete_from_dict(d: dict[str, int], k: str):
            if k not in d:
                pass
            elif d[k] == 1:
                del d[k]
            else:
                d[k] -= 1

        t_dict = Counter(t)
        i = 0

        res = None

        while i < len(s):
            if s[i] in t_dict:
                start = i

                tmp_dict = t_dict.copy()

                while i < len(s) and any(tmp_dict):
                    delete_from_dict(tmp_dict, s[i])
                    i += 1

                if not any(tmp_dict):
                    if not res:
                        res = s[start: i]
                    else:
                        res = s[start: i] if len(res) > len(s[start: i]) else res

            i += 1

        return '' if not res else res
