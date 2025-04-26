class Array: 
    def __init__(self, array: list = []):
        self.array = array
    def push(self, a):
        self.array.append(a)
    def __str__(self):
        return str(self.array)
    def pop(self):
        self.array.pop()
    


arr = Array()

arr.push("e")
arr.push("a")
arr.push("6")
arr.push("g")
arr.push("g")
arr.pop()

print(arr)