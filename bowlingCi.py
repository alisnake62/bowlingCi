from typing import List
import random

class Frame:

    _lancers:List[int]

    def __init__(self) -> None:
        self._lancers = []

    def lancer(self, nombreDeQuille:int=None) -> None:
        if nombreDeQuille is None:
            nombreDeQuille = random.randint(0, 10)
        self._lancers.append(nombreDeQuille)

class Partie:

    _frames:List[Frame]

    def __init__(self) -> None:
        self._frames = []

    def lancer(self, nombreDeQuille:int=None) -> None:
        frame = Frame()
        frame.lancer(nombreDeQuille=nombreDeQuille)
        self._frames.append(frame)

    def getScore(self) -> int:
        score = 0
        for frame in self._frames:
            for lancer in frame._lancers:
                score += lancer
        return score