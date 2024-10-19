import os
try:
    open("bufor_serwera", "x")
except FileExistsError:
    pass

while(True):
    with open("bufor_serwera", "r+") as bufor:
        lines = bufor.readlines()

        if len(lines)!=0:
            filename = lines[0].replace("\n", "")
            del lines[0]
            contents = ""

            for line in lines:
                if ";" in line:
                    print(line.replace(";", ""))
                else: 
                    print(line)
                contents += line


            with open(filename, "a") as response:
                response.write(contents)
            

            bufor.truncate(0)
            
            try:
                os.remove(".lockfile")
            except OSError:
                pass
      