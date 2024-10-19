import os
loopOn = True

while(loopOn):
    
    f = open("dane.txt", "r+")
    f.seek(0, os.SEEK_END)
    
    if f.tell()==0:
        num = input()
        f.write(str(num))
        # zapisuje dane i czeka na odp
    else:
        q = open("wyniki.txt", "r+")
        q.seek(0, os.SEEK_END)
        if q.tell==0:
            pass
        else:
            print("tutaj")
            wynik = q.readline()
            print("wynik: ",wynik)
            q.close()
            
            f.close()
            loopOn=False
    
        q.close()
        f.close()
 