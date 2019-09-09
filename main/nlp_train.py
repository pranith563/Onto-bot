from rasa.nlu.training_data import load_data
from rasa.nlu.model import Trainer
from rasa.nlu import config,components,registry
from rasa.nlu.model import Interpreter
from rasa.nlu.extractors.crf_entity_extractor import CRFEntityExtractor
from rasa.nlu.extractors import EntityExtractor
import sys

def load_training_data(data_file="../data/testData.json",config_file="../configs/config_spacy.yml"):
	training_data = load_data(data_file)
	trainer = Trainer(config.load(config_file))
	trainer.train(training_data)
	model_directory = trainer.persist('./projects/default/')
	
	# where model_directory points to the model folder
	return model_directory


def load_entity_extractor(data_file,config_file):
	training_data = load_data(data_file)
	configuration = config.load(config_file)
	comp_builder = components.ComponentBuilder()
	#component = comp_builder.create_component("ner_crf",configuration)
	#ee = EntityExtractor(components.Component(configuration))
	crf = CRFEntityExtractor()
	crf.train(training_data,configuration)
	model_directory = crf.persist('./models/default/')
	return model_directory

