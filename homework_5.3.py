import string
user_text = input("Введіть текст:")
for symbol in string.punctuation:    #набір розділових знаків, зміни на пробіли
    user_text = user_text.replace(symbol, " ")
words = user_text.split() #окремі слова
hashtag = ""
for word in words:
    hashtag += word.capitalize() #слова з великої літери
final_hashtag = "#" + hashtag
if len(final_hashtag) > 140:
    final_hashtag = final_hashtag[:140] #обрізання рядка до 140 символів
print(final_hashtag)