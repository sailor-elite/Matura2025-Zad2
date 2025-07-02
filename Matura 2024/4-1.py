plik = open("liczby_przyklad.txt", "r")

tablica = []
tablica_liczby  = []
tablica_dzielniki = []
wynik_dzielniki = 0
j = 0
i = 0


for linia in plik:
    linia = linia.strip()
    linia = linia.split()
    tablica.append(linia)
for dzielnik in range (0,len(tablica[0])):
    tablica_dzielniki.append(tablica[0][dzielnik])

for liczba in range(0, len(tablica[1])):
    tablica_liczby.append(tablica[1][liczba])

    while i != len(tablica_liczby):
        while j < len(tablica_dzielniki):
            s = tablica_liczby[i]
            j = j +1
            print (s)
        i = i +1







