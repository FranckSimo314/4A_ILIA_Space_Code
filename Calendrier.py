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


