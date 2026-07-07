# ==========================
# WORD COUNTER
# ==========================

# Counts the number of words
def number_of_word(text):
    words = len(text.split())
    return words

# Counts characters excluding spaces
def characters_without_whitespaces(text):
    words_without_whitespace = text.replace(" ", "")
    return len(words_without_whitespace)

# Counts all characters including spaces
def characters_with_whitespaces(text):
    return len(text)

print("===== WORD COUNTER =====")
text = input("Enter some text:\n")

print(number_of_word(text))
print(characters_without_whitespaces(text))
print(characters_with_whitespaces(text))