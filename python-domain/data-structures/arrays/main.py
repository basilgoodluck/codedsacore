class Array: 
    def __init__(self, array: list = []):
        self.array = array
    def push(self, element):
        self.array.append(element)
    def pop(self):
        last_element = self.array[-1]
        self.array.pop()
        return last_element
    def shift(self):
        first_element = self.array[0]
        self.array.pop(0)
        return first_element
    def unshift(self, element):
        return self.array.insert(0, element)
    def length(self):
        return len(self.array)
    def insert(self, index, element):
        self.array.insert(index, element)
    def delete(self, element):
        self.array.remove(element)
    def slice(self, key):
        if isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step
            return self.array[start:stop:step]
        return self.array[0:key]
    def __str__(self):
        return str(self.array)