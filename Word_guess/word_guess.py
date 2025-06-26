import random

word_bank = ['rizz', 'ohio', 'skibidi', 'tom', 'holberton', 'france', 'bordeaux', 'ordinateur', 'vayres', 'enceinte', 'maison', 'telephone', 'codedex']
word = random.choice(word_bank)
guess_word = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guess_word))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guess_word[i] = guess  # corrected assignment
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guess_word:
        print('\nCongratulations! You guessed the word: ' + word)
        break
else:
    print('\nYou ran out of attempts! The word was: ' + word)
