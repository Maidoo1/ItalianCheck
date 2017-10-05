import words
from random import randint
import time


class Language:
    def __init__(self):
        self.non_stop = True
        self.to_rus = False
        self.dict = words.big_dict
        self.string1 = ''
        self.string2 = ''
    
    def rand_num(self):
        return randint(1, len(self.dict))

    def pass_words(self, num):        
        print('%s : ' % self.dict[num][self.to_rus], end='')
        response = str(input())

        return response
    
    def answer(self, response, word):
        if response == '':
            self.non_stop = False
        elif response == word:
            print('Верно!\n')
        else:
            print('Даун! Правильно - %s\n' % word)
        
    def _verb_end(self, rus_end, new_words, number, code=3):
        num = randint(0, 7)
        endings = words.endings
        
        new_words[0] = new_words[0][:-code] + endings[number][num]
        new_words[1] = new_words[1][:-3] + endings[4][num]
        
        print('%s : ' % new_words[self.to_rus], end='')
        response = str(input())

        self.answer(response, new_words[not self.to_rus])
            
    def translate_verb(self):
        self.dict = words.verbs
        num = randint(1, len(self.dict))
        
        new_words = [self.dict[num][0], self.dict[num][1]]
        rus_end = new_words[0][-3:]
        
        endings = words.endings
          
        if rus_end == 'ать':
            self._verb_end(rus_end, new_words, 2, 2)
        elif rus_end == 'ить' or rus_end == 'еть':
            self._verb_end(rus_end, new_words, 1)
        else:
            self._verb_end(rus_end, new_words, 3)
        
    def translate(self):
        num = self.rand_num()

        response = self.pass_words(num)
        
        self.answer(response, self.dict[num][not self.to_rus])
    '''
    def translate_sents(self):
        self.dict = words.pronouns

        num = randint(1, len(self.dict))
        self.string1 += self.dict[num][0] + ' '
        self.string2 += self.dict[num][1] + ' '

        num1 = randint(1, len(words.verbs))
        self.string1 += words.verbs[num1][0][:-3]
        self.string1 += words.endings[1][num]
        self.string2 += words.verbs[num1][1][:-3]
        self.string2 += words.endings[4][num]
        
        print('%s : ' % self.string1, end='')
        response = str(input())
        if response == self.string2:
            print('Красава братан\n')
            self.string1 = ''
            self.string2 = ''
        else:
            print('Ну ты и даун.\nПравильно %s\n' % self.string2)
            self.string1 = ''
            self.string2 = ''
        #response = self.pass_words(num)
        #self.answer(response, self.dict[num][not self.foreign_to_rus])
        '''

language = Language()
language.foreign_to_rus = False
print('Здарова, дегенерат! Хочешь поучить итальянский? '
      'Ну тогда угадывай слова, как можешь! '
      'Кстати, чтобы закончить цикл, нажми кнопочку enter, не вводя слова.\n')

while language.non_stop:
    language.translate()
