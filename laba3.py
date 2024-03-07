words = []
while True:
    word = input("Введите слово (или 'стоп' для завершения): ")
    if word.lower() == 'стоп':
        break
    words.append(word)
result = ' '.join(words)
print("Результат:", result)
