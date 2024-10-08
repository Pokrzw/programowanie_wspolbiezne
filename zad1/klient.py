loopOn = True
while(loopOn):
    f = open("dane.txt", "w")
    num = input()
    print(num)
    f.write(num)
    f.close()
    # loopOn= False