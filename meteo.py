# New Python file
"""
Scrivi un programma in Python che risolva il seguente problema:

Creazione di un elenco di Città (4 punti)
Elaborazione del Meteo (5 punti)
Stampa con calcolo finale (3 punti)
"""
import random
def crea_luoghi(n):
  """
  Crea una funzione crea_luoghi che:
Riceve come parametro un numero intero n.
Chiede all'utente di inserire i nomi di n città.
Restituisce i nomi inseriti sotto forma di lista.
  """
  l = []
  n = int(input("Dimmi un numero di città che vuoi inserire per controllarne il meteo "))
  for i in range (0, n):
    citta = input("Dimmi il nome di una città ")
    l.append(citta)
  return l


def elabora_meteo (l):
  """
  Crea una funzione elabora_meteo che per ogni città presente nella lista ricevuta come parametro:
Genera casualmente la temperatura in gradi (da -5 a 35) utilizzando la funzione randint(min, max) del modulo random.
La temperatura va memorizzata in un dizionario come valore con chiave il nome della città.
  """
  d = {}
  for citta in l:
    t = random.randint(-5, 35)
    print(f"La temperatura a {citta} è di {t}")
    d[citta] = t
  return d

def stampa_meteo (d):
    """
    Crea una funzione stampa_meteo che per ogni città presente nel dizionario ricevuto come parametro:
Visualizza a schermo il nome della città, la sua temperatura e una valutazione testuale a seconda di un range (polare, freddo, fresco, caldo, afa) con un'emoji collegata.
Calcola e stampa la temperatura media dell'elenco delle città.
    """
  for i in range(len(d)):
    if t<=0:
      print(f"{citta} oggi ha una meteo polare 🧊")
    elif t>0 and t<=7:
      print(f"{citta} oggi ha una meteo freddo ❄️")
    elif t>7 and t<= 13:
      print(f"{citta} oggi ha una meteo fresco 🌬️")
    elif t>13 and t<=25:
      print(f"{citta} oggi ha una meteo caldo 🥵")
    else t>25:
      print(f"{citta} oggi ha una meteo caldo 🔥")

elenco = crea_luoghi(n)
print(elenco)
print(elabora_meteo(elenco))
print(stampa_meteo(elabora_meteo(elenco)))
            