import os
loopOn = True
while(loopOn):
    f = open("dane.txt", "r+")

    f.seek(0, os.SEEK_END)
    if f.tell()==0:
        num = input()
        f.write(str(num))
        f.close()
    else:
        f.close()
        pass
    