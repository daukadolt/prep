class Bad:
    def __init__(self, hashval):
        self.hash = hashval
    def __hash__(self):
        return self.hash

if __name__ == "__main__":
    b = Bad(1)
    htable = {}
    htable[b] = 42
    print(htable[b])
    b.hash = 123
    print(htable[b])
