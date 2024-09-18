import unittest
from BowlingGame import BowlingGame  

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def testGutterGame(self):
        for i in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)  # Spare
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    def testOneStrike(self):
        self.game.roll(10)  # Strike
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    def testPerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)


if __name__ == '__main__':
    unittest.main()