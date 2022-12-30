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

    def test_lancer_2_3(self):
        # Arrange
        partie = Partie()

        # Action
        partie.lancer(nombreDeQuille=2)
        partie.lancer(nombreDeQuille=3)
        score = partie.getScore()

        # Assert
        self.assertEqual(score, 5)

    def test_lancer_rate(self):
        # Arrange
        partie = Partie()

        # Action
        partie.lancer(nombreDeQuille=0)
        score = partie.getScore()

        # Assert
        self.assertEqual(score, 0)

    def test_lancer_strike(self):
        # Arrange
        partie = Partie()

        # Action
        partie.lancer(nombreDeQuille=10)
        score = partie.getScore()

        # Assert
        self.assertEqual(score, 0)

if __name__ == '__main__':
    unittest.main()
