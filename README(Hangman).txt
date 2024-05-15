READ THIS BEFORE RUNNING THE hangman.py FILE

Script name: hangman.py

Purpose:
    Allows the user to play hangman

Usage Syntax:
    CTRL + F5 or running it through the file explorer.
    *Take note if opening it through VSCode, open the entire CA1 folder.

Python Ver: 
    3.10.7, should work fine with the current latest version (As of 2/1/2023)

Library/Module
    Install these modules if not installed yet
    - csv
    - random
    - datetime

FILES REQUIRED
    ComplexWords.csv
        List of complex words found here
    words.csv
        List of simple words found here
    game_setting.csv
        Game configuration can be found here
    scores.csv
        Player logs can be found here, username, score, date and time played

REFERENCES:
    https://www.programiz.com/python-programming/csv
    https://www.w3schools.io/file/python-csv-read-write/
    https://www.w3schools.com/python/python_datetime.asp
    https://docs.python.org/3/library/datetime.html
    https://docs.python.org/3/library/getpass.html
    https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/

FILE INFORMATION
The following information is related to hangman.py file. To see admin.py file's information, refer to README(admin).txt

The hangman.py file is used to allow user to play the hangman game.

-- Functions --
get_valid_name() -> Gets a valid name
get_word(difficulty, word_index) -> Gets a random word
word_meaning(difficulty, word_index) -> Gets the meaning of the random word
is_valid_guess(guess, word) -> Checks if the user's guess is valid
record_scores(player_name, score) -> Records the user's final score
read_player_output() -> Checks with the game_setting.csv to see how many players are needed to be printed
print_top_players() -> Prints out the leaderboard following the number of players read by read_player_output()
get_rounds() -> Gets the number of attempts and words per attempt
read_difficulty() -> Checks with the game_setting.csv to see what difficulty is the game supposed to be played in
game() -> The hangman game
hangman_states(lives) -> Returns the ASCII art corresponding to the player's lives
main() -> Calls all the important functions

-- HOW TO PLAY THE GAME -- 
1. After running the file, enter your player name when prompted Player: 
    *It only accepts lowercase alphabets and/or uppercase alphabets and/or "-" and/or "/"]
2. The Hangman should be printed out and gameplay should start.
3. Enter any valid character when prompted (a to z and "'")
    Note: only 1 character at a time, if you know the word, type out the entire word, however, if you guess the wrong the word your life will be deducted.
4. Continue doing so until you reach 5 incorrect guesses or you have guessed the word
5. When prompted to start next round, enter Y or y to start the next round, else enter N or n to quit the game.
    *The game will automatically record the attempt with the highest score.