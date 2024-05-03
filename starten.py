print("hoi")

var1 = 10

if var1 == 10:
	print("het is waar")

lijst = [3,5,6]

for item in lijst:
	print(item)

def mijfunctie():
	print("dit is in de functie")

class Huis:
	huisnummer = 0
	def verkopen(_self):
		print("het huis op huisnummer", _self.huisnummer)

huis1 = Huis()

huis1.huisnummer = 35

huis1.verkopen()