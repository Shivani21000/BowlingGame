class BowlingGame:
    """
    A class to represent a Bowling Game.
    """

    def __init__(self):
        """
        Initializes the BowlingGame instance with necessary attributes.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Records the number of pins knocked down in a roll.

        :param pins: The number of pins knocked down in this roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score of the game.

        :return: The total score.
        """
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
        """
        Checks if the frame at the given roll index is a strike.

        :param rollIndex: The index of the roll to check.
        :return: True if the frame is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        Checks if the frame at the given roll index is a spare.

        :param rollIndex: The index of the roll to check.
        :return: True if the frame is a spare, False otherwise.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        """
        Calculates the bonus score for a strike.

        :param rollIndex: The index of the roll to calculate the bonus for.
        :return: The bonus score for the strike.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        """
        Calculates the bonus score for a spare.

        :param rollIndex: The index of the roll to calculate the bonus for.
        :return: The bonus score for the spare.
        """
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """
        Calculates the score for a given frame.

        :param rollIndex: The index of the roll to calculate the score for.
        :return: The score for the specified frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]