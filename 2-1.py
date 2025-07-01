
plik = open ("symbole.txt", "r")

for linia in plik :
    linia = linia.strip()
    #print("palindrom: ")
    if linia == linia[::-1]:
        print (linia)
    #print(linia[0:len(linia)-1:-1])

