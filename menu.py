# New Python file

def crea_menu():
  n = int(input("Quanti piatti ci sono nel tuo ristorante? "))
  menu = {}
  for n in range (0, n):
    nome_piatto = input("Come si chiama il piatto? ")
    ingrediente_principale = input("Qual è il suo ingrediente principale? ")
    menu[nome_piatto] = ingrediente_principale
  return menu

def filtra_menu(menu):
  i = set()
  for nome_piatto in menu:
    i.add(menu[nome_piatto])
  return i

def gestisci_ingredienti(i, menu):
  while True:
    controllo = input("Digita un ingrediente per una verifica rapida: ")
    if controllo in i:
      count = 0
      for nome_piatto in menu.keys():
        if menu[nome_piatto] == controllo:
          print(f"{nome_piatto}")
          count += 1
      return (f"Ci sono {count} piatti con questo ingrediente")
      break
    else:
          count += 0
          print("Ingrediente non trovato Riprova.")
        

nuovo = crea_menu()
print(f"Il menù del tuo ristorante è composto da {nuovo}")
print(f"Gli ingredienti principali sono {filtra_menu(nuovo)}")
print(gestisci_ingredienti(filtra_menu(nuovo), nuovo))

