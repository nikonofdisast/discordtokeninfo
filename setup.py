import os

girdi = input("PIP sürümünüz? pip3/pip: ")

if  girdi == "pip3":
    os.system('pip3 install -r gerekliler.txt')
elif girdi == "pip2":
    os.system('pip install -r gerekliler.txt')
elif girdi == "":
    os.system("pip3 install -r gerekliler.txt")
else:
    print("Lütfen geçerli bir komut girin.")