import json
import os
import random
import fnmatch
import logging

from common import Intent
from common import command_sanitizer

logger = logging.getLogger(__name__)


class get_examples_for_entities(object):
    def __init__(self,df_directory="dialogflow"):
        self.df_directory = df_directory
        self.entity_eg = self.build()

    def build(self):
        intent_directory = self.df_directory + "/intents/"
        entity_eg = {}
        for file in os.listdir(intent_directory):
            if fnmatch.fnmatchcase(file, "*_usersays_*.json"):
                with open(intent_directory + file, "r") as f:
                    user_file = json.load(f)
                    for chunk in user_file:
                        for data in chunk["data"]:
                            if "meta" in chunk or "alias" in data:
                                entity_type = data.get("alias", data["meta"])
                                if entity_type != u'@sys.ignore':
                                    if str(entity_type) not in entity_eg:
                                        entity_eg[str(entity_type)] = []
                                    entity_eg[str(entity_type)].append(data["text"])
        return entity_eg


class get_intent(object):
    def __init__(self,df_directory="dialogflow"):
        self.df_directory = df_directory
        self.intents = self.build()


    def build(self):
        """
        Converts all the intents files to list of intent objects
        :param df_directory:
        :return:
        """
        intent_directory = self.df_directory + "/intents/"
        intents = []
        for file in os.listdir(intent_directory):
            if fnmatch.fnmatchcase(file, "*_usersays_*.json"):
                continue
            with open(intent_directory + file, "r", encoding="utf8") as f:
                try:
                    intent_file = json.load(f)
                    intent = Intent(intent_file)
                    intents.append(intent)
                except Exception as e:
                    logger.error("Error in loading {}\nError:{}".format(file,e))
        return intents

def write_stories_file(df_directory = "dialogflow",
                      stories_file = "data/stories.md"):

    intents = get_intent(df_directory).intents
    parameters = get_examples_for_entities(df_directory).entity_eg
    out_string = ""
    story_count = 0

    for intent in intents:
        # *Story name
        story_count += 1
        out_string += ("## Generated Story {}\n".format(story_count))
        out_string += ("* {}".format(intent.name))
        slots = []
        entities = []

        # Handling required parameters
        for entity in intent.entities:
            if entity.required == False or str(entity.name) not in parameters:
                continue
            slot = ""
            slot += "\"" + entity.name + "\": \""
            slot += random.choice(parameters[str(entity.name)]) + "\""
            slots.append(slot)
            entities.append(slot)

        # Handling contexts
        for in_context in intent.context_in:
            slot = ""
            slot += "\"" + in_context + "\": \""
            # Ideally, this should be a number b/w 0 and lifespan
            slot += "1" + "\""
            slots.append(slot)

        if len(slots)>0:
            out_string += "{"
            for slot in slots:
                out_string += slot
                if not(slot == slots[-1]):
                    out_string += ","
            out_string += "}"
        out_string += "\n"
        
        # Slot setting
        if len(entities)>0:
            for slot in entities:
                out_string += "\t- slot{" + ("{}".format(slot)) + "}\n"

        a_name = command_sanitizer(intent.action)
        out_string += ("\t- {}\n".format(a_name))
        #print("\tIn Contexts: {}".format(len(intent.context_in)))

    with open(stories_file,'w') as outfile:
        outfile.write(out_string)

if __name__ == '__main__':
    write_stories_file()