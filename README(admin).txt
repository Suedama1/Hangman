READ THIS BEFORE RUNNING THE admin.py FILE

Script name: admin.py

Purpose:
    Allows the user to display the current leaderboard and configure game settings

Usage Syntax:
    CTRL + F5 or running it through the file explorer.
    *Take note if opening it through VSCode, open the entire CA1 folder.

Python Ver: 
    3.10.7, should work fine with the current latest version (As of 2/1/2023)

Library/Module
    Install these modules if not installed yet
    - csv
    - getpass

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
    https://www.w3schools.com/python/python_dictionaries.asp


FILE INFORMATION
The following information is related to admin.py file. To see hangman.py file's information, refer to README(Hangman).txt

The admin.py file is used to configure the Hangman game.

-- Functions --
read_difficulty() -> Retrieves the difficulty for the game
add_into_csv(word, meaning) -> Adds a new word and meaning into the words.csv or ComplexWords.csv according to the difficulty set
delete_from_csv(word) -> Deletes a word from words.csv or ComplexWords.csv according to the difficulty set
edit_word_from_csv(word, new_word) -> Edits a word from words.csv or ComplexWords.csv according to the difficulty set
edit_meaning_in_csv(word, new_meaning) -> Edits a meaning from words.csv or ComplexWords.csv according to the difficulty set
configure_attempts() -> Configure the number of attempts a player gets
configure_words_per_attempt() -> Configure the number of words the player gets to guess per attempt
change_player_output() -> Configure the number of players to output once the game is over
change_password() -> Changes the password for the user "admin"
display_top_players() -> Display all the top players
admin_login() -> Allows the user to login to perform administrative functions
main_menu() -> A main menu
sub_menu() -> A sub menu
sub_sub_menu() -> A sub sub Menu

-- HOW TO USE THE MENUS -- 
1. Navigate through the menu options using the respective numbers listed
    *The user and password to access administrative functions are "admin" and "Pa$$w0rd" respectively