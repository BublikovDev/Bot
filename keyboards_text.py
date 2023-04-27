class ua_language:
    def __init__(self):
        self.name = 'test'
    def start_msg(self):
        return 'Вітаю в боті'
    def home_kb_button_1(self):
        return 'Рахунок-фактура (чек) 🧾'
    def home_kb_button_2(self):
        return '🪪 Паспорт (DE) 🇩🇪'
    def list_view(self):
        return 'Ось список:'
    def back(self):
        return 'Назад'
ua = ua_language()