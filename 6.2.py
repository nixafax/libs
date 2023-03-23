sp = {1: ["а", "в", "е", "и", "н", "о", "р", "с", "т"], 2: ["д", "к", "л", "м", "п", "у"], 3: ["б", "г", "ё", "ь", "я"], 4: ["й", "ы"], 5: ["ж", "з", "х", "ц", "ч"], 8: ["ш", "э", "ю"], 10: ["ф", "щ", "ъ"]}
word = input("Введите слово: ")
word = word.lower()
word_l = list(word)
value = 0
for i in sp:
    for a in sp[i]:
        if a in word_l:
            col = 0
            for b in word_l:
                if b == a:
                    col += 1
            value += (i * col)
print(value)

