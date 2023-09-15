from translate import Translator

Text = "moscarce and Chizaram are an item"

translator = Translator(to_lang = 'ja')

translation = translator.translate(Text)

print(translation)




li = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10, 11]

def create_tuple(x,y):
    return list(zip(x,y))