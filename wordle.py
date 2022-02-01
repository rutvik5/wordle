import re
from string import ascii_lowercase

def fill_word(indices, curr_word, res, yellow_letters):
    if curr_word.count('_') == 0:
        word = ''.join(curr_word)
        if len(yellow_letters) > 0:
            for letter in yellow_letters:
                if letter in word:
                    if word in excluded_words:
                        res.append(''.join(curr_word))
        else:
            if word in excluded_words:
                res.append(''.join(curr_word))
    
    for index in indices[::-1]:
        for letter in letters:
            player_word[index] = letter
            fill_word(indices[-2::-1], player_word, res, yellow_letters)
            player_word[index] = '_'


with open('/usr/share/dict/words', 'r') as f:
    english_words = re.sub("[^\w]", " ",  f.read()).split()

english_words = set(word for word in english_words if len(word) == 5)

letters = set(ascii_lowercase)

print('Enter word: example => "ar__e"')
player_word = input()
while len(player_word)!= 5:
    print('Enter word: example => "ar__e"')
    player_word = input()

player_word = list(player_word)
missing = player_word.count('_')
yellow_letters = []

# checks for yellow words as CAPITAL
for idx in range(len(player_word)):
    if player_word[idx].isupper():
        yellow_letters.append(player_word[idx].lower())
        player_word[idx] = '_'

indices = [idx for idx in range(len(player_word)) if player_word[idx] == '_']

res = []
exclude = ['i', 'u', 'p', 'r', 'a', 'l']

excluded_words = []
for word in english_words:
    contains = False
    for letter in exclude:
        if letter in word:
            contains = True
    if not contains:
        excluded_words.append(word)

fill_word(indices, player_word, res, yellow_letters)

print()
print("********************************")
print("Wordle predictions for today: ")
print("********************************")
print()

for word in res:
    print(word)
