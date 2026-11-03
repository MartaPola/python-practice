# New Python file
"""
Si vuole analizzare una playlist per una festa. Scrivi un programma in Python strutturato nelle seguenti funzioni:

gestisci_genere(playlist, generi_disponibili):
Chiede all'utente di digitare il nome di un genere per una verifica rapida:
Con un'istruzione if, controlla se il genere è contenuto nel set.
Se è presente: usa un ciclo for per elencare tutti i brani associati a quel genere e conta quante tracce lo compongono.
Se non è presente: informa che nessun brano corrisponde a quella categoria e suggerisce all'utente di provare con uno dei generi presenti nel set.
"""

def crea_playlist(nome):
  """
  crea_playlist():
Chiede all'utente quante canzoni sono state aggiunte alla playlist.
Con un ciclo for, acquisisce per ogni traccia:
Il titolo del brano.
Il genere musicale (es. , , , ).
Restituisce un dizionario del tipo titolo_brano: genere.
  """
  playlist = {}
  nome = input("Nome della playlist ")
  n = int(input("Inserisci il numero di canzoni che vuoi nella nuova playlist "))
  for n in range(0, n):
   titolo_brano = input("Titolo della canzone ")

   genere = input("Genere musicale ")
   playlist[titolo_brano] = genere
  return nome, playlist


def filtra_generi(playlist):
  """
  filtra_generi(playlist):Scorre il dizionario e costruisce un set contenente tutti i generi musicali presenti nella playlist.
Stampa quanti generi diversi sono rappresentati e li elenca a schermo.
Restituisce il set ottenuto.
  """
  generi = set()
  for titolo_brano in playlist.keys():
    generi.add(playlist[titolo_brano])
    titolo_brano = playlist
  return generi


elenco =crea_playlist("Festa")
print(elenco)
print(filtra_generi(elenco))