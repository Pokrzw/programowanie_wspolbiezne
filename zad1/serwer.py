loopOn = True

while(loopOn):
    f = open("dane.txt", "r+")
    val = f.readline()
    
    if val.isdigit():
        numer = int(val)
        f.truncate(0)
        f.close()

        wynik = numer*numer
        print(wynik)
        q = open("wyniki.txt", "w")
        q.truncate(0)
        q.write(str(wynik))
        q.close()
    else:
        pass
