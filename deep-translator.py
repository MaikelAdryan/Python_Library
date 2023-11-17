# pip install deep_translator
from deep_translator import GoogleTranslator

PT, EN = 'pt', 'en'

GOOGLE = GoogleTranslator(source=PT, target=EN)

NAME, AGE = 'Adryan Maikel da Cunha Kuhne', 21
TEXT = f'Olá Mundo! Meu nome é {NAME}, e tenho {AGE} anos de idade.'

translator = GOOGLE.translate(TEXT)
print(translator)
