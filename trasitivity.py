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
		have = 0
		for t2 in graph:	
			if t2[1] == p:
				if t2[0] == y and t2[2] != x and t2[0] != t2[2]:
					if(x,p,t2[2]) not in graph:
						dic[p] = 0
						#print(x,p,t2[2])
					else :
						have = 1
						#print(triple,t2,'1')	
				if t2[2] == x and t2[0] != y and t2[0] != t2[2]:
					if(t2[0],p,y) not in graph:
						dic[p] = 0
						#print(t2[0],p,y)
					else:
						have = 1
						#print(triple,t2,'2')	
				if t2[0] == x and t2[2] != y and t2[0] != t2[2]:
					if ((t2[2],p,y) not in graph )and ((y,p,t2[2]) not in graph):
						dic[p] = 0
						#print(t2[2],p,y)
					else:
						have = 1
						#print(triple,t2,'3')		
		if have == 0:
			dic[p] = 0
			print(triple)						
				
			
				
	
# 1 est transifivity, 0 est not		

for i in dic:
	print (i)
	print (dic[i])

