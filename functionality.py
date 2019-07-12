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


dic_fun = {}
subject = {}
valuer = {}
	
for pi in propertise:
	subject[pi] = set()
	valuer[pi] = []
	
for triple in graph :
	p = triple[1]
	subject[p].add(triple[0])
	valuer[p].append(triple[2])
	
for pi in propertise:
	dic_fun[pi] = len(subject[pi])/ len(valuer[pi])	
	
for pi in dic_fun:
	print(pi,': ',dic_fun[pi])	
	

		

	
		
