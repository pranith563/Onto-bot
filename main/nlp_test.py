from rasa_nlu.model import Trainer
from rasa_nlu import config

trainer = Trainer(config.load("configs/config_spacy.yml"))
model_directory = trainer.persist('./projects/default/')

from rasa_nlu.model import Interpreter

# where model_directory points to the model folder
interpreter = Interpreter.load(model_directory)

print(interpreter.parse(u"Available Programs in the Institute"))