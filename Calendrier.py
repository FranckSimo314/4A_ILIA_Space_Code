import time

# Liste globale pour stocker les événements
evenements = []

def creer_evenement(T1: float, t: float, n: str):
    """
    Crée un évènement défini par un tuple (T1, t, n)
    et l'ajoute à la liste des événements.

    Paramètres :
        T1 (float) : timestamp de départ (ex: time.time())
        t (float)  : décalage en secondes à partir de T1
        n (str)    : nom de l'évènement
    """
    evenement = (T1, t, n)
    evenements.append(evenement)
    return evenement

def evenements_chronologiques():
    """
    Retourne la liste de tous les événements triés dans l’ordre chronologique,
    c’est-à-dire selon T1 + t.
    """
    return sorted(evenements, key=lambda e: e[0] + e[1])

def premier_evenement():
    """
    Retourne le nom du premier évènement dans la liste chronologique.
    Si la liste est vide, retourne None.
    """
    if not evenements:
        return None
    triés = evenements_chronologiques()
    return triés[0][2]  # le nom de l'évènement

def prochain_evenement():
    """
    Retourne le nom du prochain évènement à venir
    par rapport au temps actuel.
    Si aucun évènement futur n’existe, retourne None.
    """
    now = time.time()
    triés = evenements_chronologiques()

    for e in triés:
        T1, t, n = e
        if T1 + t > now:
            return n  # nom du premier évènement futur

    return None
