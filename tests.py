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

    def test_lancer_2(self):
        # Arrange
        partie = Partie()

        # Action
        partie.lancer(nombreDeQuille=2)
        score = partie.getScore()

        # Assert
        self.assertEqual(score, 2)

if __name__ == '__main__':
    unittest.main()
