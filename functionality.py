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
s = set()
o = []

for pi in p :
	for triple in graph:
		if triple[1]==pi:
			s.add(triple[0])
			o.append(triple[2])
	print(pi)
	print(len(s)/len(o))
	s = set()
	o = []	
	

		

	
		
