# Задача 1 - Написати програму, в якій необхідно видалити всі вказані літери з стрінги(string)
print("Введіть текст")
line_1 = input()
print("Введіть літеру")
letter_need_to_delete = input()
final_text_1 = line_1.replace(letter_need_to_delete,"")
print(final_text_1)

# Написати програму, яка візьме string і в кожному слові замінить першу літеру на велику.

print("Введіть текст")
line_2 = input()
final_text_2 = str.title(line_2)
print(final_text_2)

#Напишіть програму яка перевертає стрінгу

print("Введіть текст, який потрібно перевенути")
line_3 = input()
final_text_3 = line_3[::-1]
print(final_text_3)

# Напишіть програму яка приймає на вхід 2 стрінги та порівнює їх

print("Введіть вихідний текст")
line_4 = input()
print("Введіть текст, який потрібно порівняти")
line_4_compare = input()
if line_4 == line_4_compare:
    print("Тексти однакові")
else:
    print("Тексти відрізняються")

# Напишіть програму яка візьме стрінг та повторить її задану кількість раз.

print("Введіть текст")
line_5 = input()
print("Введіть кількість повторів")
koef_5 = int(input())
print(line_5*koef_5)

# Написати програму для підрахунку конвертації валюти

print("Введіть сумму")
sum_6 = float(input())
print("Введіть валюту суми (UAH/USD/EUR)")
currency_1 = input()
if currency_1 != 'UAH' and currency_1 != 'USD' and currency_1 != 'EUR':
    print("Валюта введена некорректно")
else:
    print("Введіть валюту конвертації (UAH/USD/EUR)")
    currency_2 = input()
    if currency_2 != "UAH" and currency_2 != "USD" and currency_2 != "EUR":
        print("Валюта введена некорректно")
    else:
        if currency_1 == 'UAH':
            koef_1 = 1
        elif currency_1 == "USD":
            koef_1 = 38
        else:
            koef_1 = 40
        if currency_2 == 'UAH':
            koef_2 = 1
        elif currency_2 == "USD":
            koef_2 = 38
        else:
            koef_2 = 40
        sum_final = round(sum_6*koef_1/koef_2,2)
        print(sum_final,' ',currency_2)