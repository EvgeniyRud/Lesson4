# Задача 1 - Написати програму, в якій необхідно видалити всі вказані літери з стрінги(string)
print("Введіть текст")
line = input()
print("Введіть літеру")
letter_need_to_delete = input()
final_text = line.replace(letter_need_to_delete,"")
print(final_text)
