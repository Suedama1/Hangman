from word_list import wordlist, complexWordlist
import csv
import random
import datetime
# Initializes the player_name
player_name = ""


def get_valid_name():
    """This function gets a valid name from the player that includes upper and/or lowercase alphabets and/or "-" and/or "/" in their name
    """
    # Declares player_name varaible as global so that it can be modified
    global player_name
    # Sets a flag to indicate that the player name is not valid to be used in the while loop after
    valid_player_name = False
    # Keeps prompting for player's name until valid_player_name turns to true
    while not valid_player_name:
        # Prompts the player for their name
        player_name = input("Player: ")
        # If the player's name consists of only letters, hyphens, or forward slashes, only then valid_player_name will turn True and the while loop will end
        if player_name.isalpha() or "-" in player_name or "/" in player_name:
            valid_player_name = True
        else:
            # This will print out an error message if the player's name is not valid
            print(
                "Please enter a name which consists of uppercase and/or lowercase letters and/or '-' and/or '/'")


def get_word(difficulty, word_index):
    """Get the word at the specified index in the word list respective to the specified difficulty

    Args:
        difficulty (str): The difficulty level of the game
        word_index (int): The index of the word in the word list

    Returns:
        str: The word at the specified index in the word list
    """
    if difficulty == "Simple":
        word = str(wordlist[word_index]["Word"])
    elif difficulty == "Complex":
        word = str(complexWordlist[word_index]["Word"])
    return word.lower()


def word_meaning(difficulty, word_index):
    """Get the meaning of the word at the specified index in the word list respective to the specified difficulty

    Args:
        difficulty (str): The difficulty level of the game
        word_index (int): The index of the word in the word list

    Returns:
        str: The meaning of the word at the specified index in the word list
    """
    if difficulty == "Simple":
        meaning = str(wordlist[word_index]["Meaning"])
    elif difficulty == "Complex":
        meaning = str(complexWordlist[word_index]["Meaning"])
    return meaning


def is_valid_guess(guess, word):
    """Check if the given guess is a valid guess for the given word.

    Args:
        guess (str): The guess to be checked
        word (str): The word that the guess is being checked against

    Returns:
        bool: True if the guess is valid, False if not valid
    """
    # Check if the guess is a single letter or the same length as the word or if it has an apostrophe
    if (len(guess) == 1 and guess.isalpha()) or len(guess) == len(word) or "'" in guess:
        return True
    else:
        return False


def record_scores(player_name, score):
    """Record the player's name and score in the scores CSV file.


    Args:
        player_name (str): The name of the player
        score (int): The score achieved by the player
    """
    # Gets the current date
    current_date = datetime.datetime.now().date()
    # Gets the current time
    current_time = datetime.datetime.now().time()
    # Formats the current date to be Day-Month-Year
    formatted_date = current_date.strftime(
        "%d-%m-%Y")
    # Formats the current time to be Hour-Minute-Seconds
    formatted_time = current_time.strftime("%H-%M-%S")
    # Opens the csv file in append mode
    with open('scores.csv', 'a', newline='') as score_file:
        # Create a CSV writer object to write to the file
        writer = csv.writer(score_file)
        # Write the player's name, score, date, and time to the file as a new row
        writer.writerow([player_name, score, formatted_date, formatted_time])
    # Closes the score file
    score_file.close()


def read_player_output():
    """Read the number of top players to display from the game_setting.csv file

    Returns:
        int: The number of top players to display
    """
    # Open the game_setting.csv file in read mode
    with open('game_setting.csv', 'r', newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        # Get the headers of the CSV file
        headers = next(reader)
        # Find the index of the 'player_output' column
        player_output_index = headers.index('player_output')
        # Iterate through the rows in the CSV file
        for row in reader:
            # Return the value in the 'player_output' column for the first row
            return row[player_output_index]


def print_top_players():
    """Reads the scores from the scores CSV file, sorts them in descending order by score, and prints the number of top players as specified in the game settings CSV file
    """
    # Initialize an empty list to store scores
    scores = []

    # Open the scores CSV file and read its contents
    with open('scores.csv', 'r', newline='') as scores_file:
        reader = csv.reader(scores_file)
        # Skip the header row
        next(reader)
        # Iterate through each row in the file
        for row in reader:
            # Get the username and score from the row
            username = row[0]
            score = row[1]
            # Try to convert the score to an integer
            try:
                score = int(score)
            except ValueError:
                # If the score cannot be converted to an integer, skip this row
                continue
            # Add the username and score to the list
            scores.append([username, score])

    # Sort the scores in descending order by score
    scores.sort(key=lambda x: x[1], reverse=True)

    # Get the number of players to display from the game settings CSV file
    num_players = int(read_player_output())
    # If the number of players to display is not set, return
    if num_players is None:
        return
    # Print the top players
    print("Top Players:")
    # Iterate through the top `num_players` scores
    for i in range(num_players):
        # If there are no more scores left, break out of the loop
        if i >= len(scores):
            break
        # Print the player's rank, name, and score
        print(f"{i+1}. {scores[i][0]}: {scores[i][1]}")


def get_rounds():
    """Returns the number of attempts and number of words per attempt from the game setting CSV file
    
    Returns:
        int: The number of attempts and number of words per attempts
    """
    # Open the game setting CSV file in read mode
    with open('game_setting.csv', 'r') as game_setting_file:
        # Create a CSV reader object
        reader = csv.reader(game_setting_file)
        # Skip the headers row
        next(reader)
        # Iterate through the rows of the CSV file
        for row in reader:
            # Get the number of attempts and number of words per attempt from the current row
            attempts = int(row[0])
            words_per_attempt = int(row[1])
    # Return the number of attempts and number of words per attempt
    return attempts, words_per_attempt


def read_difficulty():
    """Returns the difficulty level "Simple" or "Complex"

    Returns:
        str: The difficulty level "Simple" or "Complex"
    """
    with open('game_setting.csv', 'r') as game_setting_file:
        reader = csv.reader(game_setting_file)
        # Read the headers row
        headers = next(reader)
        # Get the index of the 'difficulty' column
        difficulty_index = headers.index('difficulty')
        for row in reader:
            # Return the difficulty level from the 'difficulty' column
            return row[difficulty_index]


def game():
    # Gets the attempts and words_per_attempts from the function get_rounds
    attempts, words_per_attempt = get_rounds()
    # Creates an empty list to store the scores from each attempt
    attempt_scores = []
    # Variable to be assigned with the highest score from each attempt later
    high_score = 0
    # Gets the difficulty of the game
    difficulty = read_difficulty()
    # Loops the amount of times attempts is configured to
    for i in range(attempts):
        # Variable to be assigned with the total score attained from the current attempt, will be resetted back to zero as the loop restarts
        total_score = 0
        # Loops the amount of times words_per_attempt is configured to
        for j in range(words_per_attempt):
            # Generates a random integer from 0 to the length of the wordlist
            if difficulty == "Simple":
                word_index = random.randint(0, len(wordlist) - 1)
            else:
                word_index = random.randint(0, len(complexWordlist) - 1)
            # Gets a random word
            word = get_word(difficulty, word_index)
            # Prints out "_" equivalent to the length of the word
            number_of_letters = "_" * len(word)
            # Sets a flag to indicate that it is not correct
            is_correct = False
            # List to store the guessed letters
            guessed_letters = []
            # List to store the guessed words
            guessed_words = []
            # List to store the correct guesses
            correct_guesses = []
            # List to store the incorrect guesses
            incorrect_letters = []
            # Variable to store the lives the player has
            lives = 5
            # Variable created to add scores
            score = 0

            print("H A N G M A N!\n")
            print(f"Player: {player_name}")
            print(f"Attempt: {i+1} of {attempts}")
            print(f"Round: {j+1} of {words_per_attempt}")
            print(hangman_states(lives))
            print(f"\nIncorrect guesses:", ' '.join(incorrect_letters),
                  "(" + str(len(incorrect_letters)) + ")\n")
            print(number_of_letters)
            # While not False and lives does not equal to zero and lives bigger than zero
            while not is_correct and lives != 0 and lives >= 0:
                # Prompts the user for an input
                guess = input("Select a valid character [a-z,']: ").lower()
                # Runs through the guess with the is_valid_guess function
                if is_valid_guess(guess, word):
                    # If length of guess is 1 character only and is an alphabet
                    if len(guess) == 1 and guess.isalpha():
                        # Checks if the user has already guessed the guess before
                        if guess in guessed_letters:
                            print(f"You already guessed the letter {guess}")
                        # If the guess is not in the word, a life will be deducted, will also break out of the loop if lives is zero
                        elif guess not in word:
                            lives -= 1
                            if lives == 0:
                                break
                            # Appends the current letter to guessed_letters and incorrect_letters
                            guessed_letters.append(guess)
                            incorrect_letters.append(guess)
                        else:
                            # Appends the current letter to guessed_letters and correct_guesses
                            guessed_letters.append(guess)
                            correct_guesses.append(guess)
                            # Variable to change the number_of_letters into a list
                            word_as_list = list(number_of_letters)
                            # Get a list of indices where the guessed letter appears in the word
                            indices = [i for i, letter in enumerate(
                                word) if letter == guess]
                            # Create a set to store the counted letters
                            counted_letters = set()
                            # Iterate through the indices of the guessed letter in the word
                            for index in indices:
                                # If the guessed letter has not been counted yet add 2 scores
                                if word[index] not in counted_letters:
                                    score += 2
                                    # Add the letter to the set of counted letters
                                    counted_letters.add(word[index])
                                # Replace the underscore at the current index with the guesed letter
                                word_as_list[index] = guess
                            # Create a new string from the modified list of characters
                            number_of_letters = "".join(word_as_list)
                            # If there are no more "_" in the string, means that the word has been guessed and the flag can now be set to True to break the loop
                            if "_" not in number_of_letters:
                                is_correct = True
                    # If length of guess is equal to the length of the word and is an alphabet
                    elif len(guess) == len(word) and guess.isalpha():
                        # Checks if the user has already guessed the guess before
                        if guess in guessed_words:
                            print(f"You already guessed the letter {guess}")
                        # If the guess is not in the word, a life will be deducted, will also break out of the loop if lives is zero
                        elif guess != word:
                            print(f"{guess} is not the word.")
                            lives -= 1
                            if lives == 0:
                                break
                            # Appends the current word to guessed_letters and incorrect_letters
                            guessed_words.append(guess)
                            incorrect_letters.append(guess)
                        else:
                            # Changes the flag to True
                            is_correct = True
                            # Changes the "_" to be the word
                            number_of_letters = word
                            # Appends the current guess to correct_guesses
                            correct_guesses.append(guess)
                            # Gets the number of unique letters so it doesn't count duplicate letters
                            unique_letters = set(word) - set(guessed_letters)
                            # Gives the user the appropriate amount of scores
                            score += 2 * len(unique_letters)
                            break

                    else:
                        # This will print if the user has neither made a guess that is equivalent to 1 letter or the length of the word
                        print("Not a valid guess.")
                    # This part will print if it has failed the is_valid_guess check
                    print("H A N G M A N!\n")
                    print(f"Player: {player_name}")
                    print(f"Attempt: {i+1} of {attempts}")
                    print(f"Round: {j+1} of {words_per_attempt}")
                    print(hangman_states(lives))
                    print(f"Incorrect guesses: ", ' '.join(incorrect_letters),
                          "(" + str(len(incorrect_letters)) + ")\n")
                    print(number_of_letters)
                else:
                    print("Not a valid guess. Please try again.")
            # If the flag has been set to correct, it will print a congratulations
            if is_correct:
                print(
                    f"Congratulations. The secret Word({difficulty}) is {word}: {word_meaning(difficulty, word_index)}\n*****")
            # If the flag has not been set to correct, but the player has ran out of attempts, it will print this instead
            else:
                print(
                    f"Oops! The Word({difficulty}) was {word}: {word_meaning(difficulty, word_index)}\n*****")
            # This part of the code will cap the total score at 30
            total_score += score
            if total_score > 30:
                total_score = 30
            # This will print the total score the player currently has for this attempt
            # print(f"Total Score for: {total_score}")
        # This will append the score for this current attempt to the list
        attempt_scores.append(total_score)
        # If the player still has attempts left, this will print out the score for the current round and prompt the user if he/she wants to try again
        if i < attempts-1:
            print(f"\nTotal score for round {i+1}: {total_score}")
            print_top_players()
            while True:
                response = input(
                    "Enter [Y]es to play again or [N]o to quit: ").lower()
                if response == 'y':
                    break
                elif response == 'n':
                    if total_score > 15 and total_score < 30:
                        print(
                            f"Congrats! You won! You scored {total_score} out of 30!")
                    elif total_score == 30:
                        print(
                            "Congrats! You won! You scored a 30 out of 30, full marks!")
                    else:
                        print(
                            f"Sorry! You lost! You scored {total_score} out of 30!")
                    high_score = max(attempt_scores)
                    record_scores(player_name, high_score)
                    return
                else:
                    print('Invalid response. Please enter "Y" or "N".')
    # This will print if the user has ran out of attempts
    if total_score > 15 and total_score < 30:
        print(f"Congrats! You won! You scored {total_score} out of 30!")
    elif total_score == 30:
        print("Congrats! You won! You scored a 30 out of 30, full marks!")
    else:
        print(f"Sorry! You lost! You scored {total_score} out of 30!")
    high_score = max(attempt_scores)
    record_scores(player_name, high_score)


def hangman_states(lives):
    """Returns the ASCII art for the hangman game based on the number of lives remaining

    Args:
        lives (int): The number of lives remaining in the game

    Returns:
        str: The ASCII art for the hangman game
    """
    # Returns the hangman drawing depending on what value "lives" has
    if lives == 5:
        return '''
   _____
  |     |
  |     
  |    
  |    
  |
 _|_
|   |_______
|           |
|___________|'''
    elif lives == 4:
        return '''
   _____
  |     |
  |     o
  |     |
  | 
  |
 _|_
|   |_______
|           |
|___________|'''
    elif lives == 3:
        return '''
   _____
  |     |
  |     o
  |    /|
  |    
  |
 _|_
|   |_______
|           |
|___________|'''
    elif lives == 2:
        return '''
   _____
  |     |
  |     o
  |    /|\\
  |    
  |
 _|_
|   |_______
|           |
|___________|'''
    elif lives == 1:
        return '''
   _____
  |     |
  |     o
  |    /|\\
  |    / 
  |
 _|_
|   |_______
|           |
|___________|'''
    else:
        return '''
   _____
  |     |
  |     o
  |    /|\\
  |    / \\
  |
 _|_
|   |_______
|           |
|___________|'''


def main():
    get_valid_name()
    game()
    print_top_players()


main()
