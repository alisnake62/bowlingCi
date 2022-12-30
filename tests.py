import unittest

from bowlingCi import Partie

class TestLancer(unittest.TestCase):

    def test_lancer_random(self):
        # Arrange
        partie = Partie()

        # Action
        partie.lancer()
        score = partie.getScore()

        # Assert
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 10)



if __name__ == '__main__':
    unittest.main()
