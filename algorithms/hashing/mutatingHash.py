class DifferentHash:
    def __init__(self):
        self.hashcounter = 0
    def __hash__(self):
        self.hashcounter += 1
        return self.hashcounter
    def __repr__(self):
        return str(self.hashcounter)

if __name__ == "__main__":
    DH = DifferentHash()
    for _ in range(5):
        print(hash(DH))
    DHset = {DH, DH, DH}
    print(DHset)

    DHset.remove(DH)
