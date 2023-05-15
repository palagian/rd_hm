# 5. (необов'язкове виконання) Створити клас Bot та TelegramBot із першого завдання за допомогою функції type


def __init__(self, name):
    self.name = name

def send_message(self, message):
    print(message)

def say_name(self):
    print(self.name)

Bot = type(
    "Bot",
    (),
    {
        "__init__": __init__,
        "send_message": send_message,
        "say_name": say_name
    }
)


def set_url(self, url):
    self.url = url


def set_chat_id(self, chat_id):
    self.chat_id = chat_id


TelegramBot = type(
    "TelegramBot",
    (Bot,),
    {
        "__init__": __init__,
        "send_message": lambda self, message:print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}"),
        "say_name": say_name,
        "set_url": set_url,
        "set_chat_id": set_chat_id,
        "url": None,
        "chat_id": None
    }
)


some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message("Hello")
telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.send_message('Hello')
telegram_bot.set_chat_id(1)
telegram_bot.send_message('Hello')