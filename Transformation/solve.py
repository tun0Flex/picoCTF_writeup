#
from colorama import init
from colorama import Fore, Back, Style
enc=open("enc").read()
print(enc[0])
print(hex(ord(enc[0])))
#______
print(Fore.RED+"flag = ",end='')
for i in enc:
	print(Fore.BLUE+hex(ord(i)).lstrip("0x"),end='')
print(Fore.WHITE+" (ASCİİ encoding)")