import os
import yaml
import json
import fnmatch
import logging

from common import Intent
from common import command_sanitizer

logger = logging.getLogger(__name__)


class get_entity(object):
    def __init__(self,df_directory="dialogflow"):
        self.df_directory = df_directory
        self.entity_list = self.build()
    def build(self):
        directory = self.df_directory + "/intents/"
        entities = []
        for file in os.listdir(directory):
            if fnmatch.fnmatchcase(file, "*_usersays_*.json"):
                with open(directory + file, "r") as f:
                    chunks = json.load(f)
                    for chunk in chunks:
                        for data in chunk["data"]:
                            if "meta" in chunk or "alias" in data:
                                entity_type = data.get("alias", data["meta"])
                                if entity_type != u'@sys.ignore':
                                    entities.append(entity_type)

        # Getting unique values
        entities = list(set(entities))
        return entities

    def print_entity(self):
        for e in self.entity_list:
            print(" - {}".format(e))

    def write_to_string(self):
        string = ""
        for e in self.entity_list:
            string += ("  - {}\n".format(e))
        return string



class get_intent(object):
    def __init__(self,df_directory="dialogflow"):
        self.df_directory = df_directory
        self.intent_list = self.build()
        self.names = self.name()
        self.in_contexts = self.in_context()
        self.out_contexts = self.out_context()

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
                logger.setLevel(logging.INFO)
                print(logger)
                logger.info("Processing file: {}".format(file))
                try:
                    intent_file = json.load(f)
                    intent = Intent(intent_file)
                    intents.append(intent)
                except Exception as e:
                    logger.error("Error in loading {}\nError:{}".format(file,e))
        return intents

    def name(self):
        names = []
        for entry in self.intent_list:
            names.append(entry.name)
        return names

    def in_context(self):
        in_contexts = []
        for entry in self.intent_list:
            for e in entry.context_in:
                in_contexts.append(e)

        in_contexts = list(set(in_contexts))
        return in_contexts

    def out_context(self):
        out_contexts = []
        flag = []
        for entry in self.intent_list:
            context_obj = entry.context_out
            for c in context_obj:
                if c.name not in flag:
                    flag.append(c.name)
                    out_contexts.append(c)

        return out_contexts

    def print_intent(self):
        for intent in self.intent_list:
            print(" - {}".format(intent.name))

    def write_to_string(self):
        string = ""
        for intent in self.intent_list:
            string += (" - {}\n".format(intent.name))
        return string


class slot_type(object):
    def __init__(self,name,data_type):
        self.name = name
        self.data_type = data_type
        if data_type == "float":
            self.min_value = 0
            self.max_value = 10


class get_slot(object):
    def __init__(self,out_context,entity):
        self.out_context = out_context
        self.entity = entity
        self.slots = self.build()

    def build(self):
        slots = []

        # Setting entities as slot
        for entity in self.entity:
            slots.append(slot_type(entity,"text"))


        # Setting out contexts as slot
        for context in self.out_context:
            slots.append(slot_type(context.name,"float"))

        return slots

    def print_slot(self):
        for slot in self.slots:
            if slot.data_type=="float":
                print("{}:\n  type: {}\n  min_value: {}\n  max_value: {}\n".format(slot.name,slot.data_type,slot.min_value,slot.max_value))
            else:
                print("{}:\n  type: {}\n".format(slot.name,slot.data_type))

    def write_to_string(self):
        string = ""
        for slot in self.slots:
            # Contexts
            if slot.data_type=="float":
                string += ("  {}:\n    type: {}\n    min_value: {}\n    max_value: {}\n".format(slot.name,slot.data_type,slot.min_value,slot.max_value))
            # Entities
            else:
                string += ("  {}:\n    type: {}\n".format(slot.name,slot.data_type))
        
        # Requested slot
        # string += ("\t{}:\n\t\ttype: {}\n".format("requested_slot","unfeaturized"))

        return string


class get_action(object):
    def __init__(self,intent):
        self.intent = intent
        self.action = self.build()

    def build(self):
        action = []
        for intent in self.intent:
            action.append(intent.action)
            for entity in intent.entities:
                if entity.required == True:
                    action.append(intent.action + "_follow_up_" + entity.name)
        return action

    def print_action(self):
        for action in self.action:
            print("- {}".format(action))

    def write_to_string(self):
        string = ""
        for action in self.action:
            a_name = command_sanitizer(action)
            if "_follow_up_" not in a_name:
                string += ("  - action.{}\n".format(a_name))
            string += ("  - utter_{}\n".format(a_name))
        return string


def sanitize_text(text):
    new_text = ""
    dollar_flag = 0
    for i in range(len(text)):
        if text[i]=='$':
            dollar_flag = 1
            new_text = new_text + '{'
        elif dollar_flag==1 and not(text[i].isalpha() or text[i]=='_' or text[i]=='-'):
            dollar_flag = 0
            new_text = new_text + '}' + text[i]
        else:
            if text[i] in "!@#$%^&*()[]{};:,./<>?\|`~-=_+\" " or text[i].isalnum():
                new_text = new_text + text[i]
    new_text = new_text.replace("\"","\\\"")
    return new_text


class template_type(object):
    def __init__(self,name,text):
        self.name = name
        self.text = text

class get_template(object):
    def __init__(self,intent):
        self.intent = intent
        self.template = self.build()

    def build(self):
        template = []
        for entry in self.intent:
            template.append(template_type("utter_" + entry.action,entry.responses.messages))
            for entity in entry.entities:
                if entity.required == True:
                    template.append(template_type("utter_" + entry.action + "_follow_up_" + entity.name,entity.prompts))
        return template

    def print_template(self):
        for template in self.template:
            print("{}:".format(template.name))
            for text in template.text:
                if type(text) == list:
                    for t in text:
                        t = sanitize_text(t)
                        print(" - \"{}\"".format(t))
                else:
                    text = sanitize_text(text)
                    print(" - \"{}\"".format(text))

    def write_to_string(self):
        string = ""
        for template in self.template:
            t_name = command_sanitizer(template.name)
            string += (" {}:\n".format(t_name))
            for text in template.text:
                if type(text) == list:
                    for t in text:
                        t = sanitize_text(t)
                        string += ("  - \"{}\"\n".format(t))
                else:
                    text = sanitize_text(text)
                    string += ("  - \"{}\"\n".format(text))
        return string

def write_domain_file(df_directory = "dialogflow",
                      domain_file = "data/domain.yml"):
    intent = get_intent(df_directory)
    intent_str =intent.write_to_string()
    #print("intent:")
    #print(intent_str)

    entity = get_entity(df_directory)
    entity_str = entity.write_to_string()
    #print("entity:")
    #print(entity_str)

    slot = get_slot(intent.out_contexts,entity.entity_list)
    slot_str = slot.write_to_string()
    #print("slot:")
    #print(slot_str)

    template = get_template(intent.intent_list)
    template_str = template.write_to_string()
    #print("template:")
    #print(template_str)

    action = get_action(intent.intent_list)
    action_str = action.write_to_string()
    #print("action:")
    #print(action_str)

    with open(domain_file, 'w') as outfile:
        if len(slot_str)>0:
            outfile.write("slots:\n{}\n".format(slot_str))
        if len(intent_str)>0:
            outfile.write("intents:\n{}\n".format(intent_str))
        if len(entity_str)>0:
            outfile.write("entities:\n{}\n".format(entity_str))
        if len(template_str)>0:
            outfile.write("templates:\n{}\n".format(template_str))
        if len(action_str)>0:
            outfile.write("actions:\n{}\n".format(action_str))

if __name__ == '__main__':
    write_domain_file()
