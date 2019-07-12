import os
from rdflib.plugins.parsers.ntriples import NTriplesParser, Sink

	
class Stream(Sink):	
	def __init__(self):
		self.data = set()
	
	def triple(self, s, p, o):
		self.data.add((s, p, o))	
	
	def graph(self):
		return self.data	


def Filelist(filepath):
	mylist = os.listdir(filepath)
	datalist = []
	for i in mylist:
		if 'ttl' in i :
			datalist.append(i)
	return datalist	

def ChoiceType(graph,dic_dis):
	for triple in graph:
		if 'type' in triple[1]:
			if triple[2] not in dic_dis:
				dic_dis[triple[2]] = set()
			
			dic_dis[triple[2]].add (triple[0])
	
	return dic_dis	
				
	
		
# input the filepath		
datasets = Filelist('E:/python/ttldata')

print(datasets)

dic1 = {}

for filename in datasets:
	stream = Stream()
	parser = NTriplesParser(stream) 
	
	with open(filename,"rb") as data:
		parser.parse(data)
	graph = stream.graph()
	ChoiceType(graph,dic1)

	
print(dic1)	
			
for i in dic1:
	for j in dic1:
		if i == j:
			continue
		if dic1[i]&dic1[j]:
			print(i,' and ',j,' aren\'t disjunction')
		else:
			print(i,' and ',j,' are  disjunction')		



			
