from owlready2 import *
import utility as owl_paser
from rasa_nlu.model import Interpreter 
import nlp_train as nlp
import requests, base64
from requests.auth import HTTPBasicAuth
import neo as cypher

#Load the given ontology and create a graph

owl_paser.load_ontology("file:///Users/pranithreddy/Desktop/PE-2019/ontologies/iiitb/iiitb.owl")
g = default_world.as_rdflib_graph()
prefix = 'http://www.iiitb.com/ontologies/iiitb.owl'


# train the data and return a interpreter to parse queries
data_file ="../data/demo-rasa.json"

config_file="../configs/config_entity.yml"



model_directory = nlp.load_entity_extractor(data_file,config_file)
'''
model_directory = nlp.load_training_data(data_file,config_file) 
#model_directory = '/Users/pranithreddy/Desktop/PE-2019/main/./projects/default/default/model_20190423-102420'
query_parser = Interpreter.load(model_directory)



def main_sparql(interpreter=query_parser, Graph=g):
	print("Enter your query:")
	query = input()
	result = interpreter.parse(query)
	if result:
		print("Matched Intent: ", result['intent']['name'])
		entities=[]
		if result['entities']:
			for i in result['entities']:
				print("Entity: ",i['value'], i['entity'])
				value = i['value']
				first = value[0].upper()
				value = first + value[1:]
				entities.append(value)
		else:
			print("No Entities")
	else:
		print("No matching intents found")

	if entities:
		if len(entities)==1:
 			q="""
 				PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
 			PREFIX owl: <http://www.w3.org/2002/07/owl#>
 			PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
 			PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
 			PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
 			SELECT DISTINCT ?property ?value WHERE {
 			:"""+entities[0]+""" ?property ?value. filter ( ?property not in ( rdf:type ) )}"""
 			results=list(Graph.query(q))
 			for result in results:
 				print(result[0][42:], " -> ", result[1])

def parse_query(interpreter):
	print("Enter your query:")
	query = input()
	result = interpreter.parse(query)
	if result:
		print("Matched Intent: ", result['intent']['name'])
		entities={}
		if result['entities']:
			for i in result['entities']:
				print("Entity: ",i['value'], i['entity'])
				value = i['value']
				if(value=='iiitb'):
					value = 'IIITB'
				elif value=='cse':
					value = 'CSE'
				elif value == 'ece':
					value = 'ECE'
				elif value == 'imtech':
					value = 'Imtech'
				elif value == 'mtech.cse':
					value = 'Mtech.CSE'
				elif value == 'mtech.ece':
					value = 'Mtech.ECE'
				entity = i['entity']
				entities.update({entity:value})
		else:
			print("No Entities Found")
		return entities
	else:
		print("No matching intents found")
	return None


url = "http://localhost:7474/db/data/node/"
def main_cypher(interpreter=query_parser):
	loop=1
	while loop==1:
		entities = parse_query(interpreter)
		labels = cypher.getLabels(prefix)
		Nodes = []
		for entity in entities:
			if entity in labels:
				id = cypher.getId(entity, entities[entity])
				Node = cypher.getNode(id)
				Nodes.append(Node)
		if(len(Nodes)==1):
			print(Nodes)
		else:
			paths = cypher.getPaths(Nodes[1]['id'],Nodes[0]['id'])
			print("Paths")
			print(paths)
			print('----')
			print("Select a Path")	
			No_of_paths = len(paths)
			i=1	
			for path in paths:
				print("path :", i)
				i = i+1
				for node in path:
					id = node[35:]
					Node = cypher.getNode(id)
					print(Node['uri'][42:])
				print('----')
			print("Enter your choice :")
			choice = input()
			for node in paths[int(choice)-1]:
				id = node[35:]
				Node = cypher.getNode(id)
				print(Node['uri'][42:])
			
def main_cypher_v1(interpreter=query_parser):
	loop=1
	while loop==1:
		entities = parse_query(interpreter)
		labels = cypher.getLabels(prefix)
		Nodes = []
		for entity in entities:
			if entity in labels:
				id = cypher.getId(entity, entities[entity])
				Node = cypher.getNode(id)
				Nodes.append(Node)
		if(len(Nodes)==1):
			print(Nodes)
		else:
			paths = cypher.getPaths(Nodes[1]['id'], Nodes[0]['id'])
			print("Paths")
			print(paths)
			print('----')
			print("Select a Path")	
			No_of_paths = len(paths)
			i=1	
			for path in paths:
				print("path :", i)
				i = i+1
				node = path[1]
				id = node[35:]
				Node = cypher.getNode(id)
				print(Node['uri'][42:])
				print('----')
			print("Enter your choice :")
			choice = input()
			path = paths[int(choice)-1]
			if(len(path)==2):
				node = path[1]
				id = node[35:]
				Node = cypher.getNode(id)
				print(Node)
				return
			else:
				node = path[2]
			id = node[35:]
			Node = cypher.getNode(id)
			print(Node['uri'][42:])
			if(len(path)==3):
				node = path[2]
				id = node[35:]
				Node = cypher.getNode(id)
				print(Node)
				return

main_cypher_v1()
'''