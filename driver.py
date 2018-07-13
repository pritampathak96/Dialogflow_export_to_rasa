from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter

from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_nlu.model import Metadata, Interpreter

from rasa_core.channels.console import ConsoleInputChannel

logger = logging.getLogger(__name__)

def train_dialogue_init(domain_file="./data/domain.yml",
                        model_path="models/dialogue",
                        training_data_file="./data/stories.md"):

    fallback = FallbackPolicy(fallback_action_name="input_unknown",
                          core_threshold=0.1,
                          nlu_threshold=0.3)
    agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy(), fallback])

    agent.train(
            training_data_file,
            augmentation_factor = 50,
            epochs = 200,
            batch_size = 10,
            validation_split = 0.2)
            
    agent.persist(model_path)
    return agent


def train_dialogue_online(input_channel=ConsoleInputChannel(), 
                          interpreter_path ="./models/nlu/default/current", 
                          domain_file="data/domain.yml", 
                          training_data_file='data/stories.md'):

    fallback = FallbackPolicy(fallback_action_name="input_unknown",
                          core_threshold=0.1,
                          nlu_threshold=0.3)
    interpreter = RasaNLUInterpreter(interpreter_path)
    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy(), fallback], interpreter=interpreter)
    agent.train_online(training_data_file, 
                       input_channel=input_channel, 
                       batch_size=50, epochs=50)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data =load_data("data/training_data.json")
    trainer = Trainer(config.load("config_spacy.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")

    return model_directory


def test_nlu():
    interpreter = Interpreter.load('./models/nlu/default/current')
    while 1:
        text = input("Enter query: ")
        print(interpreter.parse(text))


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue-init","train-dialogue-online", "run","test-nlu"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue-init":
        train_dialogue_init()
    elif task == "train-dialogue-online":
        train_dialogue_online()
    elif task == "run":
        run()
    elif task == "test-nlu":
        test_nlu()
