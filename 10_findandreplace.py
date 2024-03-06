"""implement the common find and replace string function in python
Params:
1. text = str containing with all the text
2. oldText = str is the subset of text being replaced
3. newText = str with replacement text for oldText

The text is context sensitive

"""
# the argument is passed to the function and assigned as the value to the parameter

def findAndReplace(text, oldText, newText):
    replacedText = ''
    counter = 0
    while counter < len(text):
        if text[counter:counter + len(newText)] == oldText:
            replacedText += newText
            counter += len(newText)
        else:
            replacedText += text[counter]
            counter += 1
    return replacedText

assert findAndReplace('The fox', 'f', 'd') == 'The dox'
assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'