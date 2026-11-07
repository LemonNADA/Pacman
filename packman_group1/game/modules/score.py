class PlayerScore:
    def __init__(self):
        self.score = 0

    def increase_score(self, points):
        self.score += points

    def substraction_score(self,points):
        self.score-=points

    def get_current_score(self):
        return self.score
    
    def newgame_score(self):
        self.score=0

if __name__ == "__main__":
    player = PlayerScore()