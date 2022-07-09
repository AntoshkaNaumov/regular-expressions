import re
import requests

# Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов
emails = """zuck26@facebook.com  
page33@google.com  
jeff42@amazon.com"""
pattern = r'(\w+)@([a-z0-9]+)\.([a-z]{2,4})'
print(re.findall(pattern, emails, flags=re.IGNORECASE))

# Извлеките все слова, начинающиеся с ‘b’ или ‘B’ из данного текста
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""

print(re.findall(r'(\bB\w+)', text, flags=re.IGNORECASE))

# Уберите все символы пунктуации из предложения
sentence = """A, very very; irregular_sentence"""
print(" ".join(re.split('[;,\s_]+', sentence)))

# Очистите следующий твит, чтобы он содержал только одно сообщение пользователя.
# То есть, удалите все URL, хэштеги, упоминания, пунктуацию, RT и CC.
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
def clean_tweet(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()&+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
    tweet = re.sub('\s+', ' ', tweet)
    return tweet

print(clean_tweet(tweet))

# Извлеките все текстовые фрагменты между тегами с HTML страницы:
# https://raw.githubusercontent.com/selva86/datasets/master/sample.html
# Код для извлечения HTML страницы:

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text # здесь хранится html
print(re.findall('<.*?>(.*)</.*?>', r.text))

def get_number(number: str) -> str:

    if re.fullmatch(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', number):
        return 'Private'
    if re.match(r'^\w\w\d\d\d\d\d\d?$', number):
        return 'Taxi'
    return 'Fail'

#print(get_number('С227НА777'))
#КУ22777
#print(get_number('КУ22777'))

text = '''Он --- серо-буро-малиновая редиска!!
>>>:->
А не кот.
www.kot.ru'''

result = re.findall(r"\b\w[\w-]*\b", text)
#print(result)
#print(len(result))

text = "Карта map и объкт bitmap - это разные вещи"
match = re.findall("map", text) # поиск подстроки map
match = re.findall("\\bmap\\b", text)
match = re.findall(r"\bmap\b", text)
print(match)

text = "еда, беда, победа"
match = re.findall(r"(еда)", text) # использование сохраняющих скобок
print(match)

# [] симввольные классы
text = "Еда, беду, победа"
match = re.findall(r"[еЕ]д[ау]", text)
print(match)

text = "Еда, беду, 55 победа"
match = re.findall(r"[0-9]", text) # поиск вхождения цифры 5
print(match)

text = "Еда, беду, -5 55 победа"
match = re.findall(r"[-0-9][0-9]", text) # поиск вхождения цифры 5
print(match)

text = "Еда, беду, -5 55 победа"
match = re.findall(r"\d", text) # поиск вхождения всех цифр
print(match)

text = "0xf, 0xa, 0x5"
match = re.findall(r"0x[\da-fA-F]", text)
print(match)

text = "Google, Gooogle, Goooooogle"
match = re.findall(r"o{2,5}", text)
print(match)

text = "Google, Gooogle, Goooooogle"
match = re.findall(r"o{2,5}?", text) # минорный квантификатор
print(match)

phone = "89123456789"
match = re.findall(r"8\d{10}", phone) # отображение любого числа 10 раз
print(match)

text = "стеклянный, стекляный"
match = re.findall(r"стеклянн?ый", text)
print(match)

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"\w+\s*=\s*[^;]+", text)
print(match)

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"(\w+)\s*=\s*([^;]+)", text) # получим кортежи из ключа и значения
print(match)

text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img.*?>", text) # ? использование минорного квантификатора
print(match)

text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img[^>]*>", text) # ? использование мажорного квантификатора
print(match)

text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text)
print(match)

text = "lat = 5, lon=7"
match = re.findall(r"\w+\s*=\s*\d+", text)
print(match)

text = "lat = 5, lon=7"
match = re.findall(r"lat+\s*=\s*\d+|lon\s*=\s*\d+", text)
print(match)

text = "lat = 5, lon=7, a=5"
match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text) # использование группирующих скобок не сохраняющая
print(match)

text = "lat = 5, lon=7, a=5"
match = re.findall(r"((lat|lon)\s*=\s*\d+)", text) # использование группирующих скобок сохраняющая
print(match)

text = "lat = 5, lon=7, a=5"
match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
print(match)

text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)
print(match)

text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text)
print(match)
