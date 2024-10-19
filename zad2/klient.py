import os.path
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--nazwa', '-n')
nazwa_pliku = parser.parse_args().nazwa

while True:
    try:
        open(".lockfile", "x")
        break
    except FileExistsError:
        print("Serwer zajęty, proszę czekać")
        time.sleep(1)
   
noEndtext = True
wiadomosc = ""
print("Wpisz wiadomość (wpisz ; jezeli chcesz skonczyc wpisywanie):")
while(noEndtext):
    text = input()
    wiadomosc += str(text) + "\n"
    if ";" in text:
        noEndtext = False

bufor_file = open("bufor_serwera", "w")
bufor_file.write(nazwa_pliku + '\n' + wiadomosc)
bufor_file.close()

 
# os.path.isfile(".lockfile")


# with open(".lockfile", "w+") as lockfile:
#     print("Serwer zajęty, proszę czekać")

