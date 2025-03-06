import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index,row) in df.iterrows()}
word = input('Enter a word: ').upper()
word_list = [x for x in word]
output = [phonetic_dict[letter] for letter in word_list]
print(output)