import time
from Calendrier import *

def test_creer_evenement():
    evenements.clear()  # vide la liste pour chaque test
    T1 = time.time()
    e = creer_evenement(T1, 10, "Test")
    assert e in evenements
    assert e[2] == "Test"

