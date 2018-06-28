from rasa_nlu.training_data import load_data

def build(df_directory="dialogflow",
          training_data="data/training_data.md"):

    data = load_data(df_directory)
    with open(training_data, 'w') as outfile:
            outfile.write(data.as_markdown())

if __name__ == '__main__':
    build()