loopOn = True

while(loopOn):
    f = open("dane.txt", "r")
    val = f.readline()
    
    if val.isdigit():
        numer = int(val)
        f.close()

        wynik = numer*numer + 3*numer
        print(wynik)
        q = open("wyniki.txt", "w")
        q.write(str(wynik))
        q.close()
    else:
        pass
    