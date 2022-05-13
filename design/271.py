class Codec:
    def encode(self, strs: [str]) -> str:
        return ''.join([f'{len(s)}:{s}' for s in strs])

    def decode(self, s: str) -> [str]:
        result = []
        while s:
            length, s = s.split(':', 1)
            result.append(s[:int(length)])
            s = s[int(length):]
        return result
