import re

text_ = """Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""


def generate_sentence(text: str):
    text = text.replace('\n', ' ')
    lst = list(re.findall(r"""(?:^|! |\? |\. )(\w*)""", text))
    str_=' '.join(lst).rstrip()
    return str_.capitalize()+'.'

print(generate_sentence(text_))
