user_text = input("Введите текст:")

user_words = user_text.split(" ")
count_words = [len(word) for word in user_words]
index_max, index_min = count_words.index(max(count_words)), count_words.index(min(count_words))
result = ' '.join(
    [word for index, word in enumerate(user_words) if index != index_max and index != index_min]
)
print(result)