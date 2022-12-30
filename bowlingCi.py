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
        self._carreaux              = []

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

    def getScore(self) -> int:
        score = 0
        for carreau in self._carreaux:
            if carreau.estUnStrike():
                continue
            if carreau.estUnSpare():
                continue
            for lancer in carreau._lancers:
                score += lancer
        return score