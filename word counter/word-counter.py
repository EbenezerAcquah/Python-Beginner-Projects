# ==========================
# WORD COUNTER
# ==========================
def number_of_word (text):
    words = len(text.split())
    return words

def characters_without_whitespaces(text):
    words_without_whitespace = text.replace(" ", "")
    return  len(words_without_whitespace)

def characters_with_whitespaces(text):
    return len(text)

print("===== WORD COUNTER =====")
text = input("Enter some text:\n")

print(number_of_word(text))
print(characters_without_whitespaces(text))
print(characters_with_whitespaces(text))

