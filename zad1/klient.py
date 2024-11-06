import os
loopOn = True

while True:
    f = open("dane.txt", "r+")
    f.seek(0, os.SEEK_END)
    
    

    if f.tell()==0:
        num = input()
        f.write(str(num))
        # zapisuje dane i czeka na odp
    f.close()
    break

while True:
    q = open("wyniki.txt", "r+")
    q.seek(0, os.SEEK_END)
    if q.tell()==0:
        q.close()
        continue
    else:
        q.seek(0)
        wynik = q.readline()
        print("wynik: ", wynik)
        q.truncate(0)
        q.close()
        break
    
