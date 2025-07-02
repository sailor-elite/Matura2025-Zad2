plik = open("symbole.txt", "r")

tablica = []
tymczasowa_liczba = 0

wynik = 0
tymczasowy_wynik = 0
wynik_zapis = []


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
    wynik = wynik + tymczasowa_liczba
    tymczasowa_liczba = 0

tymczasowy_wynik = wynik

while (tymczasowy_wynik > 0):
    if ((tymczasowy_wynik % 3) == 0):
        wynik_zapis.append("o")
    if ((tymczasowy_wynik % 3) == 1):
        wynik_zapis.append("+")
    if ((tymczasowy_wynik % 3) == 2):
        wynik_zapis.append("*")
    tymczasowy_wynik = tymczasowy_wynik - (tymczasowy_wynik % 3)
    tymczasowy_wynik = (int(tymczasowy_wynik / 3))

print(wynik, wynik_zapis[::-1])
