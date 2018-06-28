import os
from common import Intent
from common import command_sanitizer
from domain_builder import get_intent

def build(df_directory):
    intents = get_intent(df_directory).intent_list
    with open("action_header.txt","r") as infile:
        header = infile.read()
        with open("action.py","w") as outfile:
            outfile.write(header)

    with open("replicate_action.txt","r") as infile:
        action_data = infile.read()

    with open("action.py","a") as outfile:
        for intent in intents:
            data = "\n"
            data += action_data
            data = data.replace("<action_name>",command_sanitizer(intent.action))
            data += "\n"
            outfile.write(data)

def write_action_file(df_directory = "dialogflow"):
    build(df_directory)

if __name__ == '__main__':
    write_action_file()