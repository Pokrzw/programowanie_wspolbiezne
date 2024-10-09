import os
loopOn = True
"""
1. Klient pobiera z klawiatury i zapisuje do pliku "dane": pojedynczą liczbę całkowitą.
2. Serwer pobiera liczbę z pliku, oblicza jakąś prostą funkcję arytmetyczną (np. nieduży wielomian) 
i wynik zapisuje do pliku "wyniki".
3. Klient odbiera odpowiedź z pliku, wyświetla i kończy działanie. 
4. Serwer działa nadal w pętli oczekując na kolejne zgłoszenia.
"""


while loopOn:
    
    f = open("dane.txt", "r+")
    f.seek(0, os.SEEK_END)
    
    if f.tell()!=0:
        continue

    num = input()
    f.write(str(num))
    #mozna sprawdzic zapisywanie danych w dane.txt za pomoca tail -f dane.txt
    f.close()

    while True:
        q = open("wyniki.txt", "r+")
        q.seek(0, os.SEEK_END)

        if q.tell==0:
            q.close()
        else:
            q.seek(0, os.SEEK_SET)
            wynik = q.readline()
            print(wynik)
            q.close()
            loopOn=False
            break

        
 