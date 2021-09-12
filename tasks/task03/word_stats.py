import re

texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]


def print_word_result(counts):
    print("{:<15} {:<15} {:<15}".format("word", "count", "first line"))
    for k, v in counts.items():
        values = v
        (word_occurrence, sentence_occurrence) = values
        print("{:<15} {:<15} {:<15}".format(k, word_occurrence, sentence_occurrence))


def count_for_word(word_counts):
    if word in word_counts:
        value = word_counts.get(word)
        (count_word, count_sentence) = value
        existing_count = int(count_word)
        word_counts[word] = (existing_count + 1, count_sentence)
    else:
        word_counts[word] = (1, count)


counts = {}
for count, i in enumerate(texts):
    cleaned_sentence = re.sub(r"[^a-zA-Z0-9]", " ", i)
    list_of_words = list(cleaned_sentence.lower().split())
    for word in list_of_words:
        count_for_word(counts)
    if not counts:
        print(texts)
    else:
        print_word_result(counts)
