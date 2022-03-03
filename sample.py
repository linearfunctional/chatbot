# !pip install transformers -q
import transformers
nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
def get_answer(question= "", background = None, history = None):
    return {'answer': str(nlp(transformers.Conversation(question))).split("\nbot >> ")[1]}

print(get_answer("What is your favourite course?"))

