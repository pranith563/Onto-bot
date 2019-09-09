from owlready2 import *

def load_ontology(filename=""):
	onto = get_ontology(filename)
	onto.load()
