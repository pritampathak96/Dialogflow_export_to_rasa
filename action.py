from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.channels.direct import CollectingOutputChannel

import logging

from common import command_sanitizer
from common import out_context_set
from common import intent_index


logger = logging.getLogger(__name__)
contain = intent_index()



class account_open(Action):
    def name(self):
        return 'account_open'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "account_action"
        template = dispatcher.retrieve_template("utter_"+"account_open")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class account_balance_check(Action):
    def name(self):
        return 'account_balance_check'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "accountBalance_check"
        template = dispatcher.retrieve_template("utter_"+"account_balance_check")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class ATM_Card(Action):
    def name(self):
        return 'ATM_Card'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "ATM_Card"
        template = dispatcher.retrieve_template("utter_"+"ATM_Card")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class ATM_Locations(Action):
    def name(self):
        return 'ATM_Locations'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "ATM_Locations"
        template = dispatcher.retrieve_template("utter_"+"ATM_Locations")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class Bug_Report(Action):
    def name(self):
        return 'Bug_Report'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Bug_Report"
        template = dispatcher.retrieve_template("utter_"+"Bug_Report")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class Current_Account(Action):
    def name(self):
        return 'Current_Account'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Current_Account"
        template = dispatcher.retrieve_template("utter_"+"Current_Account")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class Debit_Cards(Action):
    def name(self):
        return 'Debit_Cards'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Debit_Cards"
        template = dispatcher.retrieve_template("utter_"+"Debit_Cards")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class input_unknown(Action):
    def name(self):
        return 'input_unknown'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Default_Fallback_Intent"
        template = dispatcher.retrieve_template("utter_"+"input_unknown")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class input_welcome(Action):
    def name(self):
        return 'input_welcome'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Default_Welcome_Intent"
        template = dispatcher.retrieve_template("utter_"+"input_welcome")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class Deposit_Rates(Action):
    def name(self):
        return 'Deposit_Rates'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Deposit_Rates"
        template = dispatcher.retrieve_template("utter_"+"Deposit_Rates")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class Deposits(Action):
    def name(self):
        return 'Deposits'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Deposits"
        template = dispatcher.retrieve_template("utter_"+"Deposits")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class MasterCard_Debit_Card(Action):
    def name(self):
        return 'MasterCard_Debit_Card'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "MasterCard_Debit_Card"
        template = dispatcher.retrieve_template("utter_"+"MasterCard_Debit_Card")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class More(Action):
    def name(self):
        return 'More'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "More"
        template = dispatcher.retrieve_template("utter_"+"More")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class payment_due_amount(Action):
    def name(self):
        return 'payment_due_amount'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "payment_due_amount"
        template = dispatcher.retrieve_template("utter_"+"payment_due_amount")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class payment_due_date(Action):
    def name(self):
        return 'payment_due_date'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "payment_due_date"
        template = dispatcher.retrieve_template("utter_"+"payment_due_date")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class Retail_Banking(Action):
    def name(self):
        return 'Retail_Banking'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Retail_Banking"
        template = dispatcher.retrieve_template("utter_"+"Retail_Banking")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class Savings_Account(Action):
    def name(self):
        return 'Savings_Account'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "Savings_Account"
        template = dispatcher.retrieve_template("utter_"+"Savings_Account")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class transfer_money_no(Action):
    def name(self):
        return 'transfer_money_no'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "transfer_money___no"
        template = dispatcher.retrieve_template("utter_"+"transfer_money_no")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class transfer_money_yes(Action):
    def name(self):
        return 'transfer_money_yes'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "transfer_money___yes"
        template = dispatcher.retrieve_template("utter_"+"transfer_money_yes")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events

class transfer_money(Action):
    def name(self):
        return 'transfer_money'

    @staticmethod
    def required_fields():
        return [
                ]

    def run(self, dispatcher, tracker, domain):
        index = "transfer_money"
        template = dispatcher.retrieve_template("utter_"+"transfer_money")

        # Checking required parameters
        intent = contain.index[index]
        for entity in intent.entities:
            if entity.required == True:
                slot = entity.name
                if slot!= None:
                    slot_val = tracker.get_slot(slot)
                    if slot_val is None:
                        logger.info("Uttering the required parameter")
                        dispatcher.utter_template(command_sanitizer("utter_{}_follow_up_{}".format(self.name(),slot)))
                        events = []
                        events.append(SlotSet("requested_slot", slot))
                        return events
                        
        text = template["text"]
        modified_text = ""
        i=0
        while i < (len(text)):
            if text[i]=='{':
                j = i+1
                slot = ""
                while(text[j]!='}' and j<len(text)):
                    slot += text[j]
                    j += 1
                modified_text += tracker.get_slot(slot)
                i = j
            else:
                modified_text += text[i]
            i += 1
        dispatcher.utter_message(modified_text)
        events = []
        contexts = out_context_set(self.name)
        for c in contexts:
            events.append(SlotSet(c,1))
        events.append(SlotSet("requested_slot", None))
        return events
