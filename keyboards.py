from telebot import types
from data import ua, list_numbers
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
lang = ua

class keyboards_:
    def __init__(self, lang=ua):
        self.lang = lang
        self.back_button = types.KeyboardButton(lang.back())

    def home_kb(self):
        markup = types.ReplyKeyboardMarkup(selective=False, resize_keyboard=True)
        button1 = types.KeyboardButton(self.lang.home_kb_button_1())
        button2 = types.KeyboardButton(self.lang.home_kb_button_2())
        markup.row(button1, button2)
        return markup

    def list_view(self, name):
        markup = types.ReplyKeyboardMarkup(selective=False, resize_keyboard=True)
        numbers = list_numbers.get(name)
        if numbers:
            for number in numbers:
                button = types.KeyboardButton(f'№{number}')
                markup.row(button)
        markup.row(self.back_button)
        return markup

    def back_kb(self):
        markup = types.ReplyKeyboardMarkup(selective=False, resize_keyboard=True)
        markup.row(self.back_button)
        return markup

kb = keyboards_()