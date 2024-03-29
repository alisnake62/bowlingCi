from typing import List
import random

class Carreau:

    _lancers:List[int]

    def __init__(self) -> None:
        self._lancers = []

    def lancer(self, nombreDeQuille:int=None) -> None:
        if nombreDeQuille is None:
            nombreDeQuille = random.randint(0, 10)
        self._lancers.append(nombreDeQuille)

    def estUnStrike(self) -> bool:
        return self._lancers == [10]

    def estUnSpare(self) -> bool:
        if len(self._lancers) == 2 and sum(self._lancers) == 10:
            return True
        return False

    def estTermine(self) -> bool:
        if self.estUnStrike():
            return True
        if len(self._lancers) == 2:
            return True
        return False

class Partie:

    _carreaux:List[Carreau]

    def __init__(self) -> None:
        self._carreaux = []

    def _carreauxActuel(self) -> Carreau:
        if len(self._carreaux) == 0:
            return None
        return self._carreaux[-1]

    def lancer(self, nombreDeQuille:int=None) -> None:
        carreauActuel = self._carreauxActuel()
        if carreauActuel is None or carreauActuel.estTermine():
            carreau = Carreau()
            carreau.lancer(nombreDeQuille=nombreDeQuille)
            self._carreaux.append(carreau)
        else:
            carreauActuel.lancer(nombreDeQuille=nombreDeQuille)

    def _nombreDeLancerApresCarreau(self, indexCarreauDepart:int, indexCarreau:int, indexLancer:int) -> int:
        nombreDeLancer = 0
        for index in range(indexCarreauDepart + 1, indexCarreau + 1):
            if index == indexCarreau:
                nombreDeLancer += indexLancer + 1
            else:
                nombreDeLancer += len(self._carreaux[index])
        return nombreDeLancer

    def _estLeBonusDUnSpare(self, indexCarreau:int, indexLancer:int) -> bool:
        if indexCarreau < 1:
            return False
        if self._carreaux[indexCarreau - 1].estUnSpare():
            nombreDeLancerApresCarreau = self._nombreDeLancerApresCarreau(indexCarreauDepart=indexCarreau-1, indexCarreau=indexCarreau, indexLancer=indexLancer)
            if nombreDeLancerApresCarreau == 1:
                return True
        return False

    def _estLeBonusDUnStrike(self, indexCarreau:int, indexLancer:int) -> bool:
        if indexCarreau < 1:
            return False
        if self._carreaux[indexCarreau - 1].estUnStrike():
            nombreDeLancerApresCarreau = self._nombreDeLancerApresCarreau(indexCarreauDepart=indexCarreau-1, indexCarreau=indexCarreau, indexLancer=indexLancer)
            if nombreDeLancerApresCarreau == 2:
                return True
        return False

    def _estDansLeScopeDUnStrike(self, indexCarreau:int, indexLancer:int) -> bool:
        if indexCarreau < 1 :
            return False
        if self._carreaux[indexCarreau - 1].estUnStrike():
            nombreDeLancerApresCarreau = self._nombreDeLancerApresCarreau(indexCarreauDepart=indexCarreau-1, indexCarreau=indexCarreau, indexLancer=indexLancer)
            if nombreDeLancerApresCarreau == 1:
                return True
        return False     

    def getScore(self) -> int:
        score = 0
        for indexCarreau, carreau in enumerate(self._carreaux):
            if carreau.estUnStrike():
                continue
            if carreau.estUnSpare():
                if self._estLeBonusDUnStrike(indexCarreau=indexCarreau, indexLancer=1):
                    score += 10 + 10
                continue
            bonusStrike = 0
            for indexLancer, lancer in enumerate(carreau._lancers):
                if self._estDansLeScopeDUnStrike(indexCarreau=indexCarreau, indexLancer=indexLancer):
                    bonusStrike += lancer
                    continue
                if self._estLeBonusDUnSpare(indexCarreau=indexCarreau, indexLancer=indexLancer):
                    score += 10 + lancer
                if self._estLeBonusDUnStrike(indexCarreau=indexCarreau, indexLancer=indexLancer):
                    score += 10 + lancer + 2 * bonusStrike
                    bonusStrike = 0
                score += lancer
        return score