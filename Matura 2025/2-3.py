plik = open("symbole.txt", "r")

tablica = []
tymczasowa_liczba = 0
wynik = 0
wynik_napis = []


for linia in plik :
    linia = linia.strip()
    tablica.append(linia)


for i in range (0,len(tablica)):
    for j in range(0, 12):
        s = tablica[i][j]
        if s == 'o':
            tymczasowa_liczba = tymczasowa_liczba + ((3 ** (12 - (j+1))) * 0 )
        if s == '+':
            tymczasowa_liczba = tymczasowa_liczba + ((3 ** (12 - (j+1))) * 1 )
        if s == '*':
            tymczasowa_liczba = tymczasowa_liczba + ((3 ** (12 - (j+1))) * 2 )
    if tymczasowa_liczba > wynik:
        wynik = tymczasowa_liczba
        wynik_napis = tablica[i]
        tymczasowa_liczba = 0
    else:
        tymczasowa_liczba = 0


print(wynik, wynik_napis)