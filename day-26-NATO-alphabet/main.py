import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index,row) in df.iterrows()}
# is_valid_word = False
# while not is_valid_word: 
#   word = input('Enter a word: ').upper()
#   try:
#     output = [phonetic_dict[letter] for letter in word]
#     is_valid_word = True
#   except KeyError:
#     print('Only letters allowed')
#   else: # will run when try statement succeeds. Correct approach of error handling.
#     print(output)

# Alternatively -> recursive function calling
def generate_phonetic():
  word = input('Enter a word: ').upper()
  try:
    output = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print('Only letters allowed')
    generate_phonetic()
  else: # will run when try statement succeeds. Correct approach of error handling.
    print(output)
generate_phonetic()