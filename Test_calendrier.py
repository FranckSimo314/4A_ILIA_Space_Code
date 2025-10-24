import time
from Calendrier import *

def test_creer_evenement():
    evenements.clear()  # vide la liste pour chaque test
    T1 = time.time()
    e = creer_evenement(T1, 10, "Test")
    assert e in evenements
    assert e[2] == "Test"

def test_evenements_chronologiques():
    evenements.clear()
    T1 = time.time()
    creer_evenement(T1, 20, "B")
    creer_evenement(T1, 10, "A")
    triés = evenements_chronologiques()
    assert triés[0][2] == "A"
    assert triés[1][2] == "B"
