from rdflib.plugins.parsers.ntriples import NTriplesParser, Sink

# parsers data
class Stream(Sink):
	
	def __init__(self):
		self.data = []
	
	def triple(self, s, p, o):
		self.data.append((s, p, o))	
	
	def graph(self):
		return self.data


stream = Stream()
parser = NTriplesParser(stream) 

with open("test.ttl","rb") as data:
	parser.parse(data)
	

graph = stream.graph()	
dic = {}
o = set()

for triple in graph:
	if 'type' in triple[1]:
		if triple[2] in dic.keys():
			o = dic[triple[2]]	
		else:
			o = set()
		o.add(triple[0])
		dic[triple[2]] = o	
		
for i in dic:
	for j in dic:
		if i != j:
			if dic[i]&dic[j]:
				print(i,' and ',j,' isn\'t disjunction')
			else:
				print(i,' and ',j,' is disjunction')		
			
		
	



	
	
	

	

	
		

