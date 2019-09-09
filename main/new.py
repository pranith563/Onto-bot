from owlready2 import *
from rdflib import Namespace
onto = get_ontology("file:///Users/pranithreddy/Desktop/PE-2019/iiitb.owl")
onto.load()



#properties = list(onto.data_properties())

#print(list(onto.classes()))
#print(list(onto.get_namespace()))

#print(list(onto.individuals()))

#import rdflib


graph = default_world.as_rdflib_graph()
# graph = rdflib.Graph()
# graph.load("file:///Users/pranithreddy/Desktop/iiitb.owl")

r = list(graph.query("""
		PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
		PREFIX owl: <http://www.w3.org/2002/07/owl#>
		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
		PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
		PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
		select ?x ?p where {
 		 	:CSE (:|!:)* ?x .
  			?x ?p ?o .
  			?o (:|!:)* :IIITB .
		}
		"""))
for i in r:
	print(i[0][42:]," -> ", i[1][42:])


# print("To know more about admissions, choose from the below options.")
# print("1. Available Programs")
# print("2. Eligibility") 
# print("3. Fee")
# print("4. How to Apply")

# def getPrograms():
# 	r = list(graph.query("""
# 		PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 		PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 		PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 		PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 		PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 		SELECT ?x WHERE {
# 		?x rdf:type :Program
# 		}
# 		"""))
# 	x =1
# 	for i in r:
# 		print(x ,i[0][42:])
# 		x = x+1

# def getEligibility():
# 	print("select a Program to know Eligibility")
# 	getPrograms()
# 	ch = input()
# 	if ch == "1":
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:DT :Eligibility ?x;
#   	}"""))
# 		print(r[0][0])
# 	elif ch == '2':
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Imtech :Eligibility ?x;
#   	}"""))
# 		print(r[0][0])
# 	elif ch == '3':
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Mtech.CSE :Eligibility ?x;
#   	}"""))
# 		print(r[0][0])
# 	else:
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Mtech.ECE :Eligibility ?x;
#   	}"""))
# 		print(r[0][0])




# def getFee():
# 	print("select a Program to know Fee")
# 	getPrograms()
# 	ch = input()
# 	if ch == "1":
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:DT :Fee ?x;
#   	}"""))
# 		print(r[0][0])
# 	elif ch == '2':
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Imtech :Fee ?x;
#   	}"""))
# 		print(r[0][0])
# 	elif ch == '3':
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Mtech.CSE :Fee ?x;
#   	}"""))
# 		print(r[0][0])
# 	else:
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Mtech.ECE :Fee ?x;
#   	}"""))
# 		print(r[0][0])


# def applicationLink():
# 	print("select a Program to know Application Link")
# 	getPrograms()
# 	ch = input()
# 	if ch == "1":
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:DT :linkForApplication ?x;
#   	}"""))
# 		print(r[0][0])
# 	elif ch == '2':
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Imtech :linkForApplication ?x;
#   	}"""))
# 		print(r[0][0])
# 	elif ch == '3':
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Mtech.CSE :linkForApplication ?x;
#   	}"""))
# 		print(r[0][0])
# 	else:
# 		r=list(graph.query("""
# 	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# 	PREFIX owl: <http://www.w3.org/2002/07/owl#>
# 	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# 	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
# 	PREFIX : <http://www.iiitb.com/ontologies/iiitb.owl#>
# 	SELECT ?x WHERE{ 
# 	:Mtech.ECE :linkForApplication ?x;
#   	}"""))
# 		print(r[0][0])

# print(" Enter Your Choice")

# choice = input()

# if choice == '1':
# 	getPrograms()
# elif choice == '2':
# 	getEligibility()
# elif choice == '3':
# 	getFee()
# else:
# 	applicationLink()