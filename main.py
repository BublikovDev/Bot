from data import bot, admin_list, ua, list_numbers
from keyboards import kb
from generate import create_png
from threading import Thread
lang = ua
@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    if id in admin_list:
        bot.send_message(id, lang.start_msg(), reply_markup=kb.home_kb())

def back_fnc(id):
    bot.send_message(id, lang.start_msg(), reply_markup=kb.home_kb())

@bot.message_handler(content_types=['text'])
def text_handler(message):
    id = message.from_user.id
    text = message.text
    if id in admin_list:
        if text == lang.home_kb_button_1() or text == lang.home_kb_button_2():
            class initializating_data:
                def __init__(self):
                    self.need_params = {}
                    self.name = None
                    self.id = None
                    self.image = None
                def one(self):
                    self.name = text
                    msg = bot.send_message(id, lang.list_view(), reply_markup=kb.list_view(text))
                    bot.register_next_step_handler(msg, self.two)

                def two(self, message):
                    text = message.text
                    text = text.split('№')[-1]

                    if text in list_numbers.get(self.name):
                        self.id = text
                        self.image = create_png(text)
                        self.need_params = self.image.get_params()
                        if self.need_params:
                            msg = 'Вітаю! введіть наступні параметри\n'
                            for param in self.need_params:
                                ask = self.need_params[param].get('ask')
                                msg += f"\n{ask}"

                            msg += '\n\nУвага! Вводьте усі параметри з нового рядку'
                            mes = bot.send_message(id, msg, reply_markup=kb.back_kb())
                            bot.register_next_step_handler(mes, self.ask_all_questions)

                    else:
                        back_fnc(id)
                def ask_all_questions(self, message):
                    response = message.text
                    params = response.split('\n')
                    lendth_need = len(self.need_params)
                    if len(params) == lendth_need:
                        count = 0
                        for param in self.need_params:
                            self.need_params[param]['result'] = params[count]
                            count += 1
                        bot.send_message(id, f'Генерую по запиту {self.name} №{self.id}')
                        response = self.image.generate_temp_photo(need_params=self.need_params)
                        result = response.get('response')
                        if result:
                            photo = open(f'temp/{self.id}.png', 'rb')
                            bot.send_document(id, photo)
                        else:
                            bot.send_message(id, f'Сталась помилка при генерації\n\n{response.get("data")}')
                    else:
                        bot.send_message(id, f'Схоже ви відправили не вірні дані по запиту {self.name} №{self.id}')


            initializating_data().one()
        else:
            back_fnc(id)
if __name__ == '__main__':
    bot.polling()

