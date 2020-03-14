# Открываем файл по адресу, считываем, записываем в переменную text, закрываем файл

try:
   f = open("C:/Users/User/Documents/Университет ИИ/Базы данных/Python/ДЗ_3/text.txt", encoding = 'utf-8')
   text = f.read()
finally:
   f.close()

# №1 Очищаем текст от знаков препинания. ВАЖНО!!! Очищенный текст называем также text. При присваивании другого имени, например text1, команда почему-то не работает
# Заменяем \n на пробелы
# Удаляем тире, при этом дефисы оставляем
# Смотрим, что получилось

symb_del = '.!?,:;«»()'
for s in symb_del:
  text = text.replace(s, '')

text = text.replace ('\n', ' ')
text = text.replace (' —', '')

print ('Задание 1. Удалили знаки препинания\n', text, '\n')

# №2 Формируем list со словами (split)
# Смотрим, что получилось

words_1 = text.split()
print ('Задание 2. Список слов:\n', words_1, '\n')

# №3 Делаем все слова с нижним регистром

words_small = list (map (lambda x:x.lower(), words_1))
print ('Задание 3. Слова с нижним регистром:\n', words_small, '\n')

# №4 Формируем dict {'слово': количество слов в тексте}

count_words = {}

for w in words_small:
  count_words[w] = 0

for sym in words_small:
  count_words[sym] += 1

print ('Задание 4. Слово и частота появления его в тексте:\n', count_words, '\n')

# №5 Сортируем словарь по значениям

sort_words = dict (sorted(count_words.items(), key=lambda kv: kv[1], reverse=True))
print ('Словарь отсортирован по убыванию частоты появления слов:\n', sort_words, '\n')

# Видно сразу, что из первых 5 часто встречающихся слов частота различная, поэтому достаточно в предыдущем коде добавить [:5]
# sort_words = dict (sorted(count_words.items(), key=lambda kv: kv[1], reverse=True)[:5])

# Усложнил задачу условием, что из первых пяти наиболее встречающихся слов частота может быть одинаковая
# Тогда надо вывести все слова с одинаковой частотой
# Выведем список из частот встреч слов в тексте
# Далее найдем количество слов K, у которых частота слов находится в первых 5
val_list = list (sort_words.values())

n=1
k=0

for i in range (0,len(val_list)):
  k+=1
  if (val_list[i]) != (val_list[i+1]):
    n+=1
  if n>5:
    # Здесь же полученное K вставим в предыдущий код
    sort_words_max5 = dict (sorted(count_words.items(), key=lambda kv: kv[1], reverse=True)[:k])
    print ('Задание 5. Первые 5 наиболее часто повторяющихся слов:\n', sort_words_max5, '\n')
    break

# Выводим количество разных слов в тексте
print ('Задание 5. Количество разных слов в тексте:', len (set (words_small)), '\n')

# Задание Pro: проводим лемматизацию слов в пункте 2, т.е. приводим слова к начальной форме

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

words_normal = list (map (lambda x:(morph.parse(x)[0]).normal_form, words_small))
print ('Задание Pro. Лемматизация, т.е. приведение слов к начальной форме:\n', words_normal)