from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import str
import uuid
from datetime import datetime

from typing import Any
from typing import Dict
from typing import Text
from typing import List

from rasa_nlu.emulators import NoEmulator


class DialogflowEmulator(NoEmulator):
    def __init__(self):
        # type: () -> None

        super(DialogflowEmulator, self).__init__()
        self.name = 'api'

    def normalise_response_json(self, data):
        # type: (Dict[Text, Any]) -> Dict[Text, Any]
        """Transform data to Dialogflow format."""


        return {
            "id": str(uuid.uuid1()),
              "result": {
                "action": data['next_action'],
                "actionIncomplete": str(data['tracker']['slots']['requested_slot']!=None),
                "fulfillment": {
                  "speech": data['reply']
                },
                "metadata": {
                  "intentId": str(uuid.uuid1()),
                  "intentName": data['tracker']['latest_message']['intent']['name'],
                  "webhookForSlotFillingUsed": "false",
                  "webhookUsed": "false"
                },
                "parameters": data['tracker']['slots'],
                "resolvedQuery": data['reply'],
                "source": "agent"
              },
              "sessionId": data['tracker']['sender_id'],
              "status": {
                "code": 200,
                "errorType": "success"
              },
              "timestamp": datetime.now().isoformat()
        }