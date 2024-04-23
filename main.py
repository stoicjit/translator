from translate import Translator
translator = Translator(to_lang='ja')
with open('text.txt') as initial_text:
    text = initial_text.read()
translation = translator.translate(text)

print(translation)