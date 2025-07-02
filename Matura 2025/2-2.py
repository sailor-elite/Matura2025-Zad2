plik = open("symbole.txt", "r")

tablica = []
wyniki = []
ilosc_kwadratow = 0

for linia in plik :
    linia = linia.strip()
    tablica.append(linia)


for i in range (1,len(tablica) -1):
    for j in range (1,11):
        s = tablica[i][j]
        #print (s, "tablica nr: ", i, "znak nr:", j)
        if s == tablica[i][j-1] and s == tablica[i][j+1]:
            if s == tablica[i+1][j] and s == tablica[i-1][j]:
                if tablica[i+1][j] == tablica[i+1][j-1] and tablica[i+1][j] == tablica[i+1][j+1]:
                    if tablica[i-1][j] == tablica[i-1][j-1] and tablica[i-1][j] == tablica[i-1][j+1]:
                        ilosc_kwadratow = ilosc_kwadratow+1
                        wyniki.append(i+1)
                        wyniki.append(j+1)


print(ilosc_kwadratow,wyniki[0:ilosc_kwadratow*2:1])

plik.close()