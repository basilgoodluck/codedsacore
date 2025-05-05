import string

class String:
    def __init__(self, string: string = []):
        self.string = string
    def concat(self, item):
        return self.string + item
    def substring(self, key):
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            return self.string[start:stop:step]
        return self.string[:key]
    def length(self):
        return len(self.string)
    def indexof(self, item):
        if not self.string:
            return -1
        if not isinstance(item, str):
            raise ValueError("Item must be a string")
        if not item:
            return 0
        n = len(item)
        for i in range(len(self.string) - n + 1):
            if self.string[i:i+n] == item:
                return i
        return -1
    

