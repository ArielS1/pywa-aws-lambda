from pywa import WhatsApp, filters
from pywa.types import Message
from wa.client import wa
from wa.actions.greetings import send_random_greeting

@wa.on_message(filters.matches("Hello", "Hi", ignore_case=True))
def hello_handler(_: WhatsApp, msg: Message):
    msg.react("👋")
    msg.reply(f'Hi {msg.from_user.name} 🙋‍♂️!', quote=True)
    send_random_greeting(msg.from_user.wa_id)
    return True