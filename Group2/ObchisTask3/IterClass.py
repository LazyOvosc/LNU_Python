class IterClass:
    def __init__(self):
        self.a = 1

    def __next__(self):
        temp = self.a
        self.a += self.a*2
        return temp
        