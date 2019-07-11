from rdflib.plugins.parsers.ntriples import NTriplesParser, Sink

class Stream(Sink):
	
	def __init__(self):
		self.data = set()
	
	def triple(self, s, p, o):
		self.data.add((s, p, o))	
	
	def graph(self):
		return self.data
		
stream = Stream()
parser = NTriplesParser(stream) 

with open('test.ttl',"rb") as data:
		parser.parse(data)
	
graph = stream.graph()

propertise = set()

for triple in graph:
	propertise.add(triple[1])
	
#print(propertise)

p = list(propertise)

dic = {}

for p1 in p:
	val = propertise.copy()
	val.remove(p1)
	dic[p1] = val
	

for t1 in graph:
	x = t1[0]
	p = t1[1]
	y = t1[2]
	if len(dic[p]) != 0:
		for i in propertise:
			if i in dic[p]:
				if (y,i,x) not in graph:
					dic[p].remove(i)
			
			

# 1 est inverse, 0 est not		

for i in dic:
	print (i)
	print (dic[i])





