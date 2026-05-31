from unittest import result


def popular_words (text, words):
    bottom_text = text.lower()
    words_list = bottom_text.split()
    result = {}
    for word in words:
        count = words_list.count(word)
        result[word] = count
    return result
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' print('OK')
