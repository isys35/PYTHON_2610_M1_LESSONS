user_text = input("Введите текст:")

user_words = user_text.split(" ")
count_words = [len(word) for word in user_words]
max_words, min_words = max(count_words), min(count_words)
index_max, index_min = count_words.index(max_words), count_words.index(min_words)


# user_text.split()
# len()
# max, min
# index
# remove