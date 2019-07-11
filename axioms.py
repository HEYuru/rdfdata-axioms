from rdflib.plugins.parsers.ntriples import NTriplesParser, Sink
import csv

#  parsers data	
class Stream(Sink):
	
	def __init__(self):
		self.data = set()
	
	def triple(self, s, p, o):
		self.data.add((s, p, o))	
	
	def graph(self):
		return self.data		



# functionality 
# s is sebject.o is  object 
# time complexity = N * p
def functionality(graph,propertise):
	s = set()  
	o = []
	dic_fun = {}
	
	for pi in propertise :
		for triple in graph:
			if triple[1]==pi:
				s.add(triple[0])
				o.append(triple[2])
		dic_fun[pi] = len(s)/len(o)
		s = set()
		o = []
	return dic_fun
	

# relexivity
# time complexity = N 
def relexivity(graph,propertise):
	dic_rel = {}
	for pi in propertise:
		dic_rel[pi] = 0

# if dic_rel[p] = 1 ,p is reflexivity			
	
	for triple in graph:
		if triple[0] == triple[2]:
			dic_rel[triple[1]] = 1
			print(triple)
	
	return dic_rel
	
# symmetry
# time complexity = N*?
# if dic_sym[p] = 1 , p is symmetry
def symmetry(graph,propertise):
	dic_sym = {}
	for pi in propertise:
		dic_sym[pi] = 0
	for triple in graph:
		if dic_sym[triple[1]] == 0 and triple[0] != triple[2]:
			x = triple[0]
			p = triple[1]
			y = triple[2]
			if (y,p,x) in graph:
				dic_sym[p] = 1
				print(triple,(y,p,x))
	return dic_sym			
	
	
# transivity : p(a,b) p(b,c) p(a,c) ->>>>> 1<a,p,b>  2<b,p,c> 3<a,p,c>
# time complexity = N*N

def transivity(graph,propertise):
	prop_dict = dict()
	dic_tra = {}
	
	for pi in propertise:
		dic_tra[pi] = 0
	
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
		if dic_tra[pi] == 0:
			flag = False
			for x in prop_dict[p]:
				x_set = prop_dict[p][x]
				for y in x_set:
					if y in prop_dict[p]:
						y_set = prop_dict[p][y]
						for z in y_set:
							if z in x_set:     
								dic_tra[p] = 1
								flag = True
								print(p,x,y,z)
								break
						if flag:
							break
				if flag:
					break
					
	return dic_tra
			     						

# inverse
# time complexity = N*p
def inverse(graph,propertise):
	dic_inv = {}
	for p1 in propertise:
		dic_inv[p1] = set()
	
	for t1 in graph:
		x = t1[0]
		p = t1[1]
		y = t1[2]
		if x != y :
			for i in propertise:
				if i not in dic_inv[p] and i != p:
					if (y,i,x) in graph:
						dic_inv[p].add(i)
						print(t1,(y,i,x))
	return dic_inv					



def axioms(filename):
	stream = Stream()
	parser = NTriplesParser(stream) 
	
	with open(filename,"rb") as data:
		parser.parse(data)
		
	graph = stream.graph()
	propertise = set()
	
	for triple in graph:
		propertise.add(triple[1])
		
		
	print(propertise)
	
	dic_fun = functionality(graph,propertise)
	print('1')
	
	dic_rel = relexivity(graph,propertise)
	print('2')
	dic_sym = symmetry(graph,propertise)
	print('3')
	dic_inv = inverse(graph,propertise)
	print('4')
	dic_tra = transivity(graph,propertise)
	print('5')
	
	
	csvname = filename + '.csv'
	out = open(csvname,'a',newline='')
	csv_writer = csv.writer(out,dialect='excel')

	for pi in propertise:
		l1 = [pi]
		if(dic_fun[pi] > 0):
			l1.append('functionality')
			l1.append(dic_fun[pi])	
		
		if(dic_rel[pi] == 1):
			l1.append('relexivity')
		if(dic_sym[pi] == 1):
			l1.append('symmetry')		
		if(len(dic_inv[pi]) != 0 ):
			l1.append('inverse')	
		
		if(dic_tra[pi] == 1):
			l1.append('transivity')
		
		print(l1)
		csv_writer.writerow(l1)
	
	print('over')	
			
		
datasets = ["2015-04_persondata_de.ttl","2015-04_persondata_de"]			
	
for i in datasets:
	axioms(i)


	

