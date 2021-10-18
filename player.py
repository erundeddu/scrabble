class Player:
    def __init__(self, name):
        self.points = 0
        self.letters = []
        self.name = name

    def add_letter(self, let):
        self.letters.append(let)

    def rm_letter(self, let):
        self.letters.remove(let)

    def see_letters(self):
        return self.letters

    def add_points(self, pts):
        self.points += pts

    def get_num_letters(self):
        return len(self.letters)
