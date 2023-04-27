import re

text_ = """Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""


def generate_sentence(text: str):
    lst = re.findall(r"""(?:^|! |\? |\. )(\w*)""", text, flags=re.M)
    str_=' '.join(lst).rstrip()
    return str_.capitalize()+'.'

print(generate_sentence(text_))
