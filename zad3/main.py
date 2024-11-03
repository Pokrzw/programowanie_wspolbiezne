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
    print("___________________________")
    print(f"przerabiany plik: {nazwa_pliku}")
    print("- - - - - - - - - ")

    wystapienia = 0
    with open(nazwa_pliku, "r+") as plik:
        lines = plik.readlines()
        for line in lines:
            if line.split(" ").count(slowo)>0:
                print("Line: ",line,f"ile znaleziono {slowo}:", line.find(f'{slowo}'))
                wystapienia+=line.split(" ").count(slowo)
            if "\input" in line:
                # print(line)
                new_plik = re.findall(r'\{.*?\}', line)[0].replace('{', '').replace('}', '')
                arg1 = new_plik
                arg2 = slowo
                pid = os.fork()
                if pid>0:
                    print("Proces rodzica, czekanie na zakonczenie syna")
                    status = os.wait()
                    if os.WIFEXITED(status[1]):
                        print("Syn spadl z rowerka, ilosc slow: ", os.WEXITSTATUS(status[1]))
                        wystapienia += os.WEXITSTATUS(status[1])
                else:
                    print("Syn, moj PID:", os.getpid())
                    sys.exit(policzSlowo(arg1, arg2))
    print("- - - - - - - - - ")
    print(f"Wystapienia slowa {slowo}: {wystapienia}")
    print("___________________________")
    
    return wystapienia
            # if "\input" in line:
            #     print(line)
            #     new_plik = re.findall(r'\{.*?\}', line)[0].replace('{', '').replace('}', '')
            #     arg1 = new_plik
            #     arg2 = slowo
            #     pid = os.fork()
            #     print(new_plik)

def policzSlowoW(nazwa_pliku, slowo):
    wystapienia = policzSlowo(nazwa_pliku, slowo)
    print("Wystapienia przed tymi calymi:", wystapienia)
    # with open(nazwa_pliku, "r+") as plik:
    #     lines = plik.readlines()
    #     for line in lines:
    #         if "\input" in line:
    #             # print(line)
    #             new_plik = re.findall(r'\{.*?\}', line)[0].replace('{', '').replace('}', '')
    #             arg1 = new_plik
    #             arg2 = slowo
    #             pid = os.fork()
    #             if pid>0:
    #                 print("Proces rodzica, czekanie na zakonczenie syna")
    #                 status = os.wait()
    #                 if os.WIFEXITED(status[1]):
    #                     print("Syn spadl z rowerka, ilosc slow: ", os.WEXITSTATUS(status[1]))
    #                     wystapienia += os.WEXITSTATUS(status[1])
    #             else:
    #                 print("Syn, moj PID:", os.getpid())
    #                 sys.exit(policzSlowo(arg1, arg2))
    return wystapienia
# def countWords(nazwa_pliku, slowo):
#     with open(nazwa_pliku, "r+") as plik:
#         lines = plik.readlines()
#         for line in lines:
#             if slowo in line:
#                 wystapienia+=1
#             if "\input" in line:
#                 print(line)
#                 new_plik = re.findall(r'\{.*?\}', line)[0].replace('{', '').replace('}', '')
#                 arg1 = new_plik
#                 arg2 = slowo
#                 pid = os.fork()
#                 print(new_plik)

print(policzSlowoW(nazwa_pliku, slowo))
