# BowlingGame.py
class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):  # 10 frames in a bowling game
            if self.isStrike(rollIndex):  # Strike case
                result += self.strikeScore(rollIndex)
                rollIndex += 1  # Strike moves to the next roll
            elif self.isSpare(rollIndex):  # Spare case
                result += self.spareScore(rollIndex)
                rollIndex += 2  # Spare uses two rolls
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2  # Normal frame uses two rolls
        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]