import string

old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}


def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   input_word = input('Enter a word to score:')
   return input_word


def simple_scorer(word):
    word = word.upper()
    final_score = 0
    for char in word:
       if char in string.ascii_uppercase:
            final_score += 1     
    return final_score

def vowel_bonus_scorer(word):
    word = word.upper()
    final_score = 0
    vowels = 'AEIOU'
    for char in word:
       if char in vowels:  
           final_score += 3         
       elif char not in vowels and char in string.ascii_uppercase:
           final_score += 1

    return final_score

def scrabble_scorer(word):
    word = word.lower()
    final_score = 0 
    for char in word:
        for (key, value) in new_point_structure.items():
            if char == key:
                final_score += value
    return final_score

simple_score = {'Name':"Simple Score",
 'Description': 'Each letter is worth 1 point.',
  'Score Function':'A function with a parameter for user input that returns a score.'}
vowel_bonus = {'Name':"Bonus Vowels",
 'Description': 'Vowels are 3 pts, consonants are 1 pt.',
  'Score Function':'A function that returns a score based on the number of vowels and consonants.'}
scrabble = {'Name':"Scrabble",
 'Description': 'The traditional scoring algorithm.',
  'Score Function':'Uses the old_scrabble_scorer() function to determine the score for a given word..'}
scoring_algorithms = (simple_score, vowel_bonus, scrabble)

def scorer_prompt():
    
    print("Which scoring algorithm would you like to use?")
    choice = int(input("0 - Simple: One point per character\n1 - Vowel Bonus: Vowels are worth 3 points\n2 - Scrabble: Uses scrabble point system\nEnter 0, 1, or 2:"))
    if choice == 0:
        return scoring_algorithms[0]
    elif choice == 1:
        return scoring_algorithms[1]
    elif choice == 2:
        return scoring_algorithms[2]
    

def transform(dictionary):
    new_dictionary = {}
    for (key, value) in dictionary.items():
        for letter in value:
            letter = letter.lower()
            new_dictionary[letter] = key       
    return new_dictionary

new_point_structure = transform(old_point_structure)

def run_program():
    word = initial_prompt()
    score = 0
    user_algorithm = scorer_prompt()
    if user_algorithm == simple_score:
        score = simple_scorer(word)
    elif user_algorithm == vowel_bonus:
        score = vowel_bonus_scorer(word)
    elif user_algorithm == scrabble:
        score = scrabble_scorer(word)
       
    print(f"Score for \'{word}\': {score}")
