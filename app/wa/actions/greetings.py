from random import randint
from wa.client import wa

random_greetings = ['How are you today?', 'How can i help you?', 'Sup']

def send_random_greeting(to: str):
    wa.send_message(to, random_greetings[randint(0, len(random_greetings) - 1)])
