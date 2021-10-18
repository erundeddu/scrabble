class Letter:
    def __init__(self, char, points, amount_0):
        self.char = char
        self.points = points
        self.amount_0 = amount_0

    def get_char(self):
        return self.char

    def get_points(self):
        return self.points

    def get_amount0(self):
        return self.amount_0

    def __str__(self):
        letter_str = "(" + self.char + ", " + str(self.points) + ", " + str(self.amount_0) + ")"
        return letter_str


if __name__ == "__main__":
    a = Letter("a", 1, 12)
    print(a)
    assert a.get_char() == "a"
    assert a.get_points() == 1
    assert a.get_amount0() == 12
