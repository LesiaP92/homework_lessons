import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
      cleaned_text = ""        # змінна для очищеного тексту
      inside_tag = False       # тру якщо ми всередині тегу
      for char in html:         # перев. текс за символами
          if char == "<":
              inside_tag = True
          elif char == ">":
              inside_tag = False
          elif not inside_tag:
              cleaned_text += (
                  char
              )
      final = []            # якщо треба убираю порожні рядки
      for line in cleaned_text.splitlines():   # розбиваю текст на рядки і перебираю їх
          if line.strip():                     # метод убирає пробіли і перенос
              final.append(line)
      text = "\n".join(final)        # об`єднання рядків в текст
      with codecs.open(result_file, "w", "utf-8") as file:
          file.write(text)