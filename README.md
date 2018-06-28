# This repository converts the dialogflow export into RASA format

## Steps to prepare the files:

- Keep the dialogflow export in the `dialogflow` folder.

- `python domain_builder.py`

    This creates the domain file in data folder.

- `python story_builder.py`
    
    This creates the stories file in the data folder.

- The rasa_core files are ready.

## Steps for training:

- `python driver.py train-nlu`

- `python driver.py train-dialogue-init`

- These prepares the NLU and core models.

## Steps to run the agent:

- `python driver.py run`