spam = ['apple', 'bananas', 'tofu', 'cats']


def comma_code(items):
    sentence = ''
    for index, item in enumerate(items):
        if index == len(items) - 1:
            sentence = sentence + 'and ' + str(item) + '.'
        else:
            sentence = sentence + str(item) + ', '

    return sentence
