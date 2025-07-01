plik = open ("symbole_przyklad.txt", "r")


tablica = []

for linia in plik :
    linia = linia.strip()
    tablica.append(linia)
    #print("palindrom: ")
    #print (linia)

print(tablica)

for i in range (1, len(tablica)-1):
    for j in range (1, 11):
        s = tablica[i][j]
        print(s, "tablica nr: ", i, "znak nr: ", j)

# 1. Dokończ zadanie sprawdzając warunki tabeli (macierzy)
# 2. Przypisz zadanie do tablicy o nazwie wyniki. Wykorzystaj funkcję .append(znak)
# 3. Wypisz za pomocą pętli i print wyniki. Wyniki powinny być zapisane jako wiesz, kolumna