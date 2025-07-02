plik = open("liczby_przyklad.txt", "r")

tablica = []
tablica_liczby  = []
tablica_dzielniki = []
licznik = 0
liczba = 0

for linia in plik:
    linia = linia.strip()
    linia = linia.split()
    tablica.append(linia)
for dzielnik in range (0,len(tablica[0])):
    tablica_dzielniki.append(tablica[0][dzielnik])
for liczba in range(0, len(tablica[1])):
    tablica_liczby.append(tablica[1][liczba])


for dzielnik in tablica_dzielniki:
    for liczba in tablica_liczby:
        if int(liczba) % int(dzielnik) == 0:
            licznik += 1
            break










