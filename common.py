
def command_sanitizer(text):
    text = text.translate ({ord(c): "_" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+ "})
    return text
    

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
