import unittest

from bowlingCi import Partie

class TestLancer(unittest.TestCase):
    
    def test_lancer_random(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber un nombre de quille au hazard
        partie.lancer()
        score = partie.getScore()

        # Alors le score est compris entre 0 et 10
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 10)

    def test_lancer_2(self):
        # Etant donnée une partie
        partie = Partie()

        # On tomber 2 quilles en 1 lancer
        partie.lancer(nombreDeQuille=2)
        score = partie.getScore()

        # Alors le score est de 2
        self.assertEqual(score, 2)

    def test_lancer_2_3(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber 2 puis 3 quilles
        partie.lancer(nombreDeQuille=2)
        partie.lancer(nombreDeQuille=3)
        score = partie.getScore()

        # Alors le score est de 5
        self.assertEqual(score, 5)

    def test_lancer_rate(self):
        # Etant donnée une partie
        partie = Partie()

        # On ne fait pas tomber de quille
        partie.lancer(nombreDeQuille=0)
        score = partie.getScore()

        # Alors le socre est de 0
        self.assertEqual(score, 0)

    def test_lancer_strike(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber 10 quilles en un lancer (Strike)
        partie.lancer(nombreDeQuille=10)
        score = partie.getScore()

        # Alors le score est de 0
        self.assertEqual(score, 0)

    def test_lancer_spare(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber 10 quilles en 2 lancers (Spare)
        partie.lancer(nombreDeQuille=8)
        partie.lancer(nombreDeQuille=2)
        score = partie.getScore()

        # Alors le score est de 0
        self.assertEqual(score, 0)

    def test_1_lancer_apres_un_spare(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber 2 quilles en 1 lancer après un spare
        partie.lancer(nombreDeQuille=3)
        partie.lancer(nombreDeQuille=7) # spare
        partie.lancer(nombreDeQuille=2)
        score = partie.getScore()

        # Alors le score est de 14
        self.assertEqual(score, 14)

    def test_2_lancer_apres_un_spare(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber 2 et 5 quilles en 2 lancer après un spare
        partie.lancer(nombreDeQuille=3)
        partie.lancer(nombreDeQuille=7) # spare
        partie.lancer(nombreDeQuille=2)
        partie.lancer(nombreDeQuille=5)
        score = partie.getScore()

        # Alors le score est de 19
        self.assertEqual(score, 19)

    def test_1_lancer_apres_un_strike(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber 2 quilles en 1 lancer après un stike
        partie.lancer(nombreDeQuille=10) # strike
        partie.lancer(nombreDeQuille=2) 
        score = partie.getScore()

        # Alors le score est de 0
        self.assertEqual(score, 0)

    def test_2_lancer_apres_un_strike(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait tomber 5 quilles en 2 lancer après un stike
        partie.lancer(nombreDeQuille=10) # strike
        partie.lancer(nombreDeQuille=3)
        partie.lancer(nombreDeQuille=2)
        score = partie.getScore()

        # Alors le score est de 20
        self.assertEqual(score, 20)

    def test_1_strike_apres_un_strike(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait 1 strike après un stike
        partie.lancer(nombreDeQuille=10) # strike
        partie.lancer(nombreDeQuille=10)
        score = partie.getScore()

        # Alors le score est de 0
        self.assertEqual(score, 0)

    def test_1_spare_apres_un_strike(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait 1 spare après un stike
        partie.lancer(nombreDeQuille=10) # strike
        partie.lancer(nombreDeQuille=6)
        partie.lancer(nombreDeQuille=4)
        score = partie.getScore()

        # Alors le score est de 20
        self.assertEqual(score, 20)

    def test_1_lancer_apres_un_strike_puis_un_spare(self):
        # Etant donnée une partie
        partie = Partie()

        # On fait 1 spare après un stike
        partie.lancer(nombreDeQuille=10) # strike
        partie.lancer(nombreDeQuille=6)
        partie.lancer(nombreDeQuille=4) # spare
        partie.lancer(nombreDeQuille=4)
        score = partie.getScore()

        # Alors le score est de 38
        self.assertEqual(score, 38)

    def test_partie_complete_de_Strike(self):
        partie = Partie()

        # On fait 12 lancer de strike
        partie.lancer(nombreDeQuille=10)  # strike
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        partie.lancer(nombreDeQuille=10)
        score = partie.getScore()

        # Alors le score est de 0
        self.assertEqual(score, 0)

    def test_partie_complete(self):
        partie = Partie()

        # On fait 20 lancers
        partie.lancer(nombreDeQuille=7)
        partie.lancer(nombreDeQuille=1)
        partie.lancer(nombreDeQuille=2)
        partie.lancer(nombreDeQuille=4)
        partie.lancer(nombreDeQuille=6)
        partie.lancer(nombreDeQuille=3)
        partie.lancer(nombreDeQuille=1)
        partie.lancer(nombreDeQuille=5)
        partie.lancer(nombreDeQuille=0)
        partie.lancer(nombreDeQuille=5)
        partie.lancer(nombreDeQuille=7)
        partie.lancer(nombreDeQuille=1)
        partie.lancer(nombreDeQuille=1)
        partie.lancer(nombreDeQuille=8)
        partie.lancer(nombreDeQuille=1)
        partie.lancer(nombreDeQuille=3)
        partie.lancer(nombreDeQuille=1)
        partie.lancer(nombreDeQuille=8)
        partie.lancer(nombreDeQuille=0)
        partie.lancer(nombreDeQuille=5)
        score = partie.getScore()

        # Alors le score est de 69
        self.assertEqual(score, 69)

if __name__ == '__main__':
    unittest.main()
