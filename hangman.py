import random
import hangmanart
import hangman_wordlist

chosen_word=random.choice(hangman_wordlist.word_list).lower()
hangmanart.logo

display = []
for _ in range(len(chosen_word)):
  display += "_"

lives=6
end_of_game = False

while not end_of_game:
  guess=input("Enter a word: ").lower()

  if guess in display:
    print(f"You have already guessed {guess}  letter.")

  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter == guess:
      display[position]=guess

  if guess not in chosen_word:
    print(f"You guessed {guess}, and it does not belong to the word.You lose a life.")
    lives-=1
    if lives == 0:
      end_of_game=True
      print("GAME OVER")
      print(hangmanart.stages[0])
      print(f"The correct word was {chosen_word}")
      break

  print(display)
  if "_" not in display:
    end_of_game = True
    print("YOU WIN!")
  print(hangmanart.stages[lives])
