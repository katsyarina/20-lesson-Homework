class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)
    def print(self):
        print(self.letters)
        print(len(self.letters))

    def letters_num(self): len(self.letters)

import string

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def letters_num(self):
        return EngAlphabet.letters_num

    def is_en_letter(self, letter):
        if letter in self.letters: return True
        else: return False

    def example():
        print('Hello world')

engalphabet = EngAlphabet()
engalphabet.print()
print(engalphabet.letters_num())
print(engalphabet.is_en_letter('F'))
print(engalphabet.is_en_letter(('Щ')))
print(EngAlphabet.example())
