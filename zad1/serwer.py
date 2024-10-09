while True:
    f = open("dane.txt", "r+")
    val = f.readline()
    
    if val.isdigit():
        numer = int(val)
        f.truncate(0)
        f.close()

        wynik = numer*numer + 3*numer
        q = open("wyniki.txt", "w")
        q.write(str(wynik))
        q.close()