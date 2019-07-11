from rdflib.plugins.parsers.ntriples import NTriplesParser, Sink

class Stream(Sink):
	
	def __init__(self):
		self.data = []
	
	def triple(self, s, p, o):
		self.data.append((s, p, o))	
	
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
	
print(propertise)
p = list(propertise)
dic = {}

for pi in p:
	dic[pi] = 1

# 1 est reflexivity, 0 est not		
	
for triple in graph:
	if dic[triple[1]] == 1:
		if (triple[0],triple[1],triple[0]) not in graph:
			dic[triple[1]] = 0

for i in dic:
	print (i)
	print (dic[i])

