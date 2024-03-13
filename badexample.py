import random

class ClassName:
	"""docstring for ClassName"""
	def __init__(self, argEtt, argTvå):
		self.argEtt = argEtt
		self.argTvå = argTvå
		
def stora(list):
	steg1=max(list)
	steg2=[list.index(steg1)]
	while True:
		list.pop(steg2[-1])
		if steg1 in list:
			steg3=list.index(steg1)
			steg2.append(steg3)
		else:
			break
	return steg2

def blabla(hej):
	groda=[]
	for dag in hej:
		groda.append(dag.argTvå)
	woho=stora(groda)
	if len(woho)>1:
		return "Ingen vann!"
	else:
		return hej[woho[0]].argEtt +" vann!\n ----------------\n"


namn=["hund", "trött!!!!!!", "jag", "du", "kanske"]
p=""
objects=[]
for i in range(len(namn)):
	new=ClassName(namn[i],random.randint(1,10))
	objects.append(new)
	p+=namn[i]+": "+ str(new.argTvå)+";   "



OP=blabla(objects)

print("Resultat: "+ p+"\n" +OP)