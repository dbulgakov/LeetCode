class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val_lst = self.store.get(key, [])
        val_lst.append((timestamp, value))

        self.store[key] = val_lst

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''

        if timestamp >= self.store[key][-1][0]:
            return self.store[key][-1][1]

        left = 0
        right = len(self.store[key]) - 1
        key_values = self.store[key]

        while left <= right:
            middle = left + (right - left) // 2

            if key_values[middle][0] == timestamp:
                return key_values[middle][1]
            elif key_values[middle][0] > timestamp:
                if key_values[middle - 1][0] < timestamp:
                    return key_values[middle - 1][1]
                right = middle - 1
            else:
                if key_values[middle + 1][0] > timestamp:
                    return key_values[middle][1]
                left = middle + 1

        return ''
