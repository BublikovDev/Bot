from PIL import Image, ImageDraw, ImageFont, ImageFilter
class create_png:
    def __init__(self, filename):
        self.fileID = filename
        self.image = Image.open(f'static/{filename}.png')
        self.font_size = 11
        self.font_family = 'fonts/over.ttf'
        self.font = ImageFont.truetype(self.font_family, size=self.font_size)
        self.inserts = None
    def update_data(self, font_size=None, font_family=None):
        if font_size:
            self.font_size = font_size
        if font_family:
            self.font_family = font_family
        self.font = ImageFont.truetype(self.font_family, size=self.font_size)
    def get_params(self):
        need_params = {}
        if self.fileID == '2':
            need_params = {
                "date": {
                    'ask': '1. Введіть дату',
                    'result': None
                },
                "id": {
                    'ask': '2. Введіть номер',
                    'result': None
                },
                'name': {
                    'ask': '3. Введіть назву',
                    'result': None
                },
                'price': {
                    'ask': '4. Введіть ціну повну',
                    'result': None
                }
            }
        elif self.fileID == '3':
            need_params = {
                "date": {
                    'ask': '1. Введіть дату',
                    'result': None
                },
                'name': {
                    'ask': '2. Введіть назву',
                    'result': None
                },
                'price': {
                    'ask': '3. Введіть ціну повну',
                    'result': None
                }
            }
        elif self.fileID == '7':
            need_params = {
                "date": {
                    'ask': '1. Введіть дату',
                    'result': None
                },
                'name': {
                    'ask': '2. Введіть назву',
                    'result': None
                },
                'price': {
                    'ask': '3. Введіть ціну повну',
                    'result': None
                }
            }
        return need_params

    def config_generate(self, need_params):
        if self.fileID == '2':
            basic_font = 13
            basic_family = 'fonts/TimesNewRoman.ttf'
            padding_per_word = 6.5
            self.inserts = {
                1: {
                    'position': (107, 285),
                    'data': need_params.get('date').get("result"),
                    'font_size': basic_font,
                    'font_family': basic_family
                },
                2: {
                    'position': (150, 306),
                    'data': need_params.get('id').get("result"),
                    'font_size': basic_font,
                    'font_family': basic_family
                },
                3: {
                    'position': (240, 525),
                    'data': need_params.get('name').get("result"),
                    'font_size': 15,
                    'font_family': 'fonts/over.ttf'
                },
                4: {
                    'position': (600, 528),
                    'data': str(eval(f'{need_params.get("price").get("result")} * 0.7')),
                    'font_size': 11,
                    'font_family': 'fonts/Calibri Regular.ttf'
                },
                5: {
                    'position': (735-len(str(float(need_params.get("price").get("result"))))*0.1, 528),
                    'data': str(float(need_params.get("price").get("result"))) + ' EUR',
                    'font_size': 11,
                    'font_family': 'fonts/Calibri Regular.ttf'
                },
                6: {
                    'position': (310-(len(str(eval(f'{need_params.get("price").get("result")} * 0.25')))-1) * padding_per_word, 706),
                    'data': str(eval(f'{need_params.get("price").get("result")} * 0.25')),
                    'font_size': basic_font,
                    'font_family': basic_family
                },
                7: {
                    'position': (396-(len(str(eval(f'{need_params.get("price").get("result")} * 0.1')))-1) * padding_per_word, 706),
                    'data': str(eval(f'{need_params.get("price").get("result")} * 0.1')),
                    'font_size': basic_font,
                    'font_family': basic_family
                },
                8: {
                    'position': (482-(len(str(float(need_params.get("price").get("result"))))-1) * padding_per_word, 706),
                    'data': str(float(need_params.get("price").get("result"))),
                    'font_size': basic_font,
                    'font_family': basic_family
                },
                9: {
                    'position': (740-(len(str(float(need_params.get("price").get("result"))))-1) * padding_per_word, 690),
                    'data': need_params.get("price").get("result"),
                    'font_size': basic_font,
                    'font_family': basic_family
                }
            }
            self.font_size = basic_font
        elif self.fileID == '3':
            basic_font = 9
            basic_family = 'fonts/MuseoSans500.ttf'
            padding_per_word = 1.5
            self.inserts = {
                1: {
                    'position': (95, 437),
                    'data': need_params.get('date').get("result"),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 0,
                    'fill': '#000000',
                    'blur': 0.35
                },
                2: {
                    'position': (510, 435),
                    'data': need_params.get('date').get("result"),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 0,
                    'fill': '#000000',
                    'blur': 0.35
                },
                3: {
                   'position': (178, 660),
                   'data': need_params.get('name').get("result"),
                   'font_size': basic_font,
                   'font_family': 'fonts/MuseoSans300.ttf',
                   'angle': 0,
                   'fill': '#1c1e16',
                   'blur': 0.25
               },
                4: {
                    'position': (580, 640),
                    'data': need_params.get('price').get("result"),
                    'font_size': basic_font,
                    'font_family': 'fonts/MuseoSans500.ttf',
                    'angle': 2,
                    'fill': '#230e03',
                    'blur': 0.35
                },
                5: {
                    'position': (625, 640),
                    'data': need_params.get('price').get("result"),
                    'font_size': basic_font,
                    'font_family': 'fonts/MuseoSans500.ttf',
                    'angle': 2,
                    'fill': '#230e03',
                    'blur': 0.35
                },
            }
        elif self.fileID == '7':
            basic_font = 10
            basic_family = 'fonts/MuseoSans500.ttf'
            padding_per_word = 1.5
            self.inserts = {
                2: {
                    'position': (111, 188),
                    'data': need_params.get('date').get("result"),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': -3,
                    'fill': '#453424',
                    'blur': 0.5

                },
                4: {
                    'position': (56, 429),
                    'data': need_params.get('name').get("result"),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 1,
                    'fill': '#230e03',
                    'blur': 0.6
                },

                5: {
                    'position': (235 - (len(str(round(eval(f'{need_params.get("price").get("result")} * 0.7'), 2))) - 1)
                                 * padding_per_word, 420),
                    'data': str(round(eval(f'{need_params.get("price").get("result")} * 0.7'), 2)),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 1.8,
                    'fill': '#230e03',
                    'blur': 0.6
                },
                6: {
                    'position': (290 - (len(str(round(eval(f'{need_params.get("price").get("result")} * 0.3'), 2))) - 1)
                                 * padding_per_word, 418),
                    'data': str(round(eval(f'{need_params.get("price").get("result")} * 0.37'), 2)),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 1.8,
                    'fill': '#230e03',
                    'blur': 0.6
                },
                8: {
                    'position': (410 - (len(str(round(eval(f'{need_params.get("price").get("result")} * 1'), 2))) - 1)
                                 * padding_per_word, 414),
                    'data': str(round(eval(f'{need_params.get("price").get("result")} * 1'), 2)),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 1.8,
                    'fill': '#230e03',
                    'blur': 0.6
                },
                10: {
                    'position': (218 - (len(str(round(eval(f'{need_params.get("price").get("result")} * 0.7'), 2))) - 1)
                                 * padding_per_word, 498),
                    'data': str(round(eval(f'{need_params.get("price").get("result")} * 0.7'), 2)),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 1.8,
                    'fill': '#230e03',
                    'blur': 0.6
                },
                11: {
                    'position': (208 - (len(str(round(eval(f'{need_params.get("price").get("result")} * 0.3'), 2))) - 1)
                                 * padding_per_word, 514),
                    'data': str(round(eval(f'{need_params.get("price").get("result")} * 0.37'), 2)),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 1.8,
                    'fill': '#230e03',
                    'blur': 0.6
                },
                12: {
                    'position': (225 - (len(str(round(eval(f'{need_params.get("price").get("result")} * 1'), 2))) - 1)
                                 * padding_per_word, 529),
                    'data': str(round(eval(f'{need_params.get("price").get("result")} * 1'), 2)),
                    'font_size': basic_font,
                    'font_family': basic_family,
                    'angle': 1.8,
                    'fill': '#230e03',
                    'blur': 0.6
                }

            }
            self.font_size = basic_font
    def generate_temp_photo(self, need_params):
        try:
            if self.fileID == '2':
                self.config_generate(need_params=need_params)
                if self.inserts:
                    draw_text = ImageDraw.Draw(self.image)
                    for code in self.inserts:
                        position = self.inserts[code].get('position')
                        width = position[0]
                        height = position[-1]
                        font_size = self.inserts[code]['font_size']
                        if font_size != self.font_size:
                            self.update_data(font_size=font_size)
                        font_family = self.inserts[code]['font_family']
                        if font_family != self.font_family:
                            self.update_data(font_family=font_family)
                            print(font_family)
                        data = self.inserts[code].get('data')
                        angle = self.inserts[code].get('angle')
                        if angle:
                            temp_image = Image.new('RGBA', (500,200), (0,0,0,0))
                            draw_text = ImageDraw.Draw(temp_image)
                            draw_text.text(
                                (0, 0),
                                data,
                                font=self.font,
                                fill='#000000',
                            )
                            temp_image.rotate(angle)
                            self.image.paste(temp_image, (width, height), temp_image)

                        else:
                            draw_text.text(
                                            (width, height),
                                            data,
                                            font=self.font,
                                            fill='#000000',
                                            )
                        if 'font_size' in self.inserts[code]:
                            self.update_data()
                self.image.show()
                self.image.save(f'temp/{self.fileID}.png')
            elif self.fileID == '7' or self.fileID == '3':

                self.config_generate(need_params=need_params)
                if self.inserts:
                    draw_text = ImageDraw.Draw(self.image)
                    for code in self.inserts:
                        position = self.inserts[code].get('position')
                        width = int(position[0])
                        height = int(position[-1])
                        font_size = self.inserts[code]['font_size']
                        if font_size != self.font_size:
                            self.update_data(font_size=font_size)
                        font_family = self.inserts[code]['font_family']
                        if font_family != self.font_family:
                            self.update_data(font_family=font_family)
                            print(font_family)
                        data = self.inserts[code].get('data')
                        angle = self.inserts[code].get('angle')
                        fill = self.inserts[code].get('fill')
                        blur = self.inserts[code].get('blur')
                        if not fill:
                            fill = '#000000'
                        temp_image = Image.new('RGBA', (500,200), (0,0,0,0))
                        draw_text = ImageDraw.Draw(temp_image)
                        draw_text.text(
                            (0, 0),
                            data,
                            font=self.font,
                            fill=fill,
                        )
                        #print(angle)
                        if angle:
                            temp_image = temp_image.rotate(angle, expand=True)
                        if blur:
                            temp_image = temp_image.filter(ImageFilter.GaussianBlur(radius=blur))
                        #temp_image.show()
                        self.image.paste(temp_image, (width, height), temp_image)


                        if 'font_size' in self.inserts[code]:
                            self.update_data()
                self.image.show()
                self.image.save(f'temp/{self.fileID}.png')
            return {'response': True}
        except Exception as a:
            raise a
            return {'response': False, 'data': str(a)}

#need_params = {'date': {'ask': '1. Введіть дату', 'result': '23.07.2015'}, 'id': {'ask': '2. Введіть номер', 'result': '132131'}, 'name': {'ask': '3. Введіть назву', 'result': 'Versandkosten'}, 'price': {'ask': '4. Введіть ціну повну', 'result': '400'}}
need_params = {'date': {'ask': '1.', 'result': '12.02.2012'}, 'name': {"ask": None, 'result': 'APPLE Air Pods Pro'}, 'price': {'result': '295.45'}}
create_png('3').generate_temp_photo(need_params=need_params)