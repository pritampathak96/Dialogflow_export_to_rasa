import os
import json
import fnmatch
import logging

logger = logging.getLogger(__name__)


def command_sanitizer(text):
    text = text.translate ({ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+ "})
    return text

def out_context_set(action_name,df_directory="dialogflow"):
    intent_directory = df_directory + "/intents/"
    contexts = []
    for file in os.listdir(intent_directory):
        if fnmatch.fnmatchcase(file, "*_usersays_*.json"):
            continue
        with open(intent_directory + file, "r", encoding="utf8") as f:
            try:
                intent_file = json.load(f)
                intent = Intent(intent_file)
                if command_sanitizer(intent.action)==action_name:
                    for context in intent.context_out:
                        contexts.append(context.name)
            except Exception as e:
                logger.error("Error in loading {}\nError:{}".format(file,e))

    return contexts

def check_for_entities(text,slot_type):
        slot = slot_index()
        s_index = slot.index
        entity = entity_index()
        e_index = entity.index
        modified_text = None
        logger.info("Slot: {} and text: {}".format(slot_type,text))
        if "sys" not in s_index[slot_type]:
            if s_index[slot_type] in e_index:
                # text parsing
                flag = 0
                entries = e_index[s_index[slot_type]]
                for key in entries:
                    for entry in entries[key]:
                        for syn in entry["synonyms"]:
                            if syn in text:
                                modified_text = entry["value"]
                                flag=1
                                break
                        if flag is 1:
                            break
                    if flag is 1:
                        break
        else:
            modified_text = text
        return modified_text
    

class Intent:
    def __init__(self, intent_export):
        self.name = intent_export["name"]
        # Getting the intent json
        intent_json = intent_export["responses"][0]

        # Getting the action name
        self.action = intent_json.get("action", self.name)

        # Parameters act as both entities and slots
        self.entities = [Entity(params) for params in intent_json["parameters"]]

        # Contexts should be treated as unfeaturized slots
        self.context_in = [context_in for context_in in intent_export["contexts"]]
        self.context_out = [OutContext(context) for context in intent_json["affectedContexts"]]

        # Messages list
        self.responses = Responses(intent_json["messages"])


class Entity:
    def __init__(self, entity_json):
        self.name = entity_json["name"]
        self.datatype = entity_json["dataType"]
        self.required = entity_json.get("required",False)
        self.prompts =[prompt["value"] for prompt in entity_json.get("prompts",[])]
        self.value = entity_json["value"]


class OutContext:
    def __init__(self, out_context_json):
        self.name = out_context_json["name"]
        # This needs to be taken care of->
        self.lifespan = out_context_json["lifespan"]


class Responses:
    def __init__(self, response_json):
        self.messages = []
        for prompt in response_json:
            if "speech" in prompt:
                self.messages.append(prompt["speech"])


class intent_index(object):
    def __init__(self):
        self.index = {}
        self.intents = []
        self.build()
    def build(self,df_directory="dialogflow"):
        intent_directory = df_directory + "/intents/"
        for file in os.listdir(intent_directory):
            if fnmatch.fnmatchcase(file, "*_usersays_*.json"):
                continue
            with open(intent_directory + file, "r", encoding="utf8") as f:
                logger.info("Processing file: {}".format(file))
                try:
                    intent_file = json.load(f)
                    intent = Intent(intent_file)
                    self.index[command_sanitizer(intent.name)] = intent
                    self.intents.append(intent)
                except Exception as e:
                    logger.error("Error in loading {}\nError:{}".format(file,e))

    def getobj(index_name):
        return index[index_name]

class entity_index(object):
    def __init__(self):
        self.index = {}
        self.build()

    def build(self,df_directory="dialogflow"):
        entity_directory = df_directory + "/entities/"
        for file in os.listdir(entity_directory):
            if fnmatch.fnmatchcase(file, "*_entries_*.json"):
                with open(entity_directory + file, "r", encoding="utf8") as f:
                    logger.info("Processing file: {}".format(file))
                    try:
                        entity_file = json.load(f)
                        entity_name = file[0:file.find("_entries_")]
                        entries = []
                        for entry in entity_file:
                            entries.append(entry)
                        self.index[entity_name] = entries
                    except Exception as e:
                        logger.error("Error in loading {}\nError:{}".format(file,e))


class slot_index(object):
    def __init__(self):
        self.index = {}
        self.build()

    def build(self):
        intent = intent_index()
        for i in intent.intents:
            for e in i.entities:
                self.index[e.name] = e.datatype[1:]
