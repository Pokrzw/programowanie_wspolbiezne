import argparse
import os
import sys
import re

parser = argparse.ArgumentParser()
parser.add_argument('--poczatek', '-p')
parser.add_argument('--slowo', '-s')
nazwa_pliku =  parser.parse_args().poczatek
slowo =  parser.parse_args().slowo

# print("Slowo: "+ slowo +", nazwa:"+ nazwa_pliku)
def policzSlowo(nazwa_pliku, slowo):
    wystapienia = 0
    forks = 0
    with open(nazwa_pliku, "r+") as plik:
        lines = plik.readlines()
        for line in lines:
            if line.split(" ").count(slowo)>0:
                wystapienia+=line.split(" ").count(slowo)
            if "\input" in line:
                new_plik = re.findall(r'\{.*?\}', line)[0].replace('{', '').replace('}', '')
                arg1 = new_plik
                arg2 = slowo
                pid = os.fork()
                if pid>0:
                    forks += 1
                else:
                    sys.exit(policzSlowo(arg1, arg2))
    for i in range(forks):
        child_pid, status = os.wait()
        if os.WIFEXITED(status):
            wystapienia += os.WEXITSTATUS(status)

    return wystapienia


def policzSlowoW(nazwa_pliku, slowo):
    wystapienia = policzSlowo(nazwa_pliku, slowo)
    return wystapienia


print(f"W tekscie slowo {slowo} wystepuje {policzSlowoW(nazwa_pliku, slowo)} razy")
