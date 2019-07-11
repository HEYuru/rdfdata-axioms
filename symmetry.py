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

with open('2014-09_persondata_de.ttl',"rb") as data:
		parser.parse(data)
	

graph = stream.graph()

propertise = set()
for triple in graph:
	propertise.add(triple[1])
	
print(propertise)
p = list(propertise)
dic = {}

for pi in p:
	dic[pi] = 1

for triple in graph:
	if dic[triple[1]] == 1:
		x = triple[0]
		p = triple[1]
		y = triple[2]
		if (y,p,x) not in graph:
			dic[p] = 0
	
# 1 est symmetry, 0 est not		

for i in dic:
	print (i)
	print (dic[i])


