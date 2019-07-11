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

prop_dict = dict()
prop_result = set()

for triple in graph:
	x = triple[0]
	p = triple[1]
	y = triple[2]
	
	if x == y:
		continue
		
	if p not in prop_dict:
		prop_dict[p] = dict()
	
	tmp_dict = prop_dict[p]
	
	if x not in tmp_dict:
		tmp_dict[x] = set()
	
	tmp_set = tmp_dict[x]
	tmp_set.add(y)

	
print('1')	

	
for p in prop_dict:
	flag = False
	for x in prop_dict[p]:
		x_set = prop_dict[p][x]
		for y in x_set:
			if y in prop_dict[p]:
				y_set = prop_dict[p][y]
				for z in y_set:
					if z in x_set:     
						prop_result.add(p)
						flag = True
						print(p,x,y,z)
						break
				if flag:
					break
		if flag:
			break

print (prop_result)
			
	


