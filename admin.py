import csv
import getpass


def read_difficulty():
    """Gets the difficulty from game_setting.csv

    Returns:
        Returns the difficulty "Simple" or "Complex" 
    """
    with open('game_setting.csv', 'r') as game_setting_file:
        reader = csv.reader(game_setting_file)
        headers = next(reader)
        difficulty_index = headers.index('difficulty')
        for row in reader:
            return row[difficulty_index]


# Initializes the difficulty level to the value returned from read_difficulty()
difficulty = read_difficulty()


def add_into_csv(word, meaning):
    """
    Adds a word into the CSV file respective to its difficulty

    Args:
        word (str): The word to be added to the CSV file
        meaning (str): The meaning of the word to be added to the CSV file
    """
    # Sets a flag to indicate that the word does not word_exists
    word_exists = False
    if difficulty == "Simple":
        with open('words.csv', 'r', newline='') as wordsfile:
            reader = csv.reader(wordsfile)
            for row in reader:
                # Set word_exists to True if word is found in the CSV file
                if row[0] == word:
                    word_exists = True
                    break
        # If the word does not exist, append it to the CSV file
        if not word_exists:
            with open('words.csv', 'a', newline='') as wordsfile:
                writer = csv.writer(wordsfile)
                writer.writerow([word, meaning])
            wordsfile.close()
        # If the word already exists, print an error message
        else:
            print(f"Error: word '{word}' already exists in the CSV file")
    else:
        with open('ComplexWords.csv', 'r', newline='') as wordsfile:
            reader = csv.reader(wordsfile)
            for row in reader:
                # Set word_exists to True if word is found in the CSV file
                if row[0] == word:
                    word_exists = True
                    break
        # If the word does not exist, append it to the CSV file
        if not word_exists:
            with open('ComplexWords.csv', 'a', newline='') as wordsfile:
                writer = csv.writer(wordsfile)
                writer.writerow([word, meaning])
            wordsfile.close()
        # If the word already exists, print an error message
        else:
            print(f"Error: word '{word}' already exists in the CSV file")


def delete_from_csv(word):
    """Deletes a word from the csv file respective to its difficulty

    Args:
        word (str): The word to be deleted
    """
    # Convert word to lowercase
    word = word.lower()
    # Sets a flag to indicate that the word does not word_exists
    word_exists = False
    if difficulty == "Simple":
        with open('words.csv', 'r', newline='') as wordsfile:
            reader = csv.reader(wordsfile)
            for row in reader:
                # Set word_exists to True if word is found in the CSV file
                if row[0].lower() == word:
                    word_exists = True
                    break
        # If the word exists, delete it from the CSV file
        if word_exists:
            # Initialize an empty list to store the rows of the CSV file
            rows = []
            with open('words.csv', 'r', newline='') as wordsfile:
                reader = csv.reader(wordsfile)
                for row in reader:
                    # Only append rows with words that are not equal to the word to be deleted
                    if row[0].lower() != word:
                        rows.append(row)
            # Overwrite the CSV file with the rows without the word to be deleted
            with open('words.csv', 'w', newline='') as wordsfile:
                writer = csv.writer(wordsfile)
                for row in rows:
                    writer.writerow(row)
        # If the word does not exist, print an error message
        else:
            print(f"Error: word '{word}' does not exist in the CSV file")
    else:
        with open('ComplexWords.csv', 'r', newline='') as wordsfile:
            reader = csv.reader(wordsfile)
            for row in reader:
                # Set word_exists to True if word is found in the CSV file
                if row[0].lower() == word:
                    word_exists = True
                    break
        # If the word exists, delete it from the CSV file
        if word_exists:
            # Initialize an empty list to store the rows of the CSV file
            rows = []
            with open('ComplexWords.csv', 'r', newline='') as wordsfile:
                reader = csv.reader(wordsfile)
                for row in reader:
                    # Only append rows with words that are not equal to the word to be deleted
                    if row[0].lower() != word:
                        rows.append(row)
            # Overwrite the CSV file with the rows without the word to be deleted
            with open('ComplexWords.csv', 'w', newline='') as wordsfile:
                writer = csv.writer(wordsfile)
                for row in rows:
                    writer.writerow(row)
        # If the word does not exist, print an error message
        else:
            print(f"Error: word '{word}' does not exist in the CSV file")


def edit_word_from_csv(word, new_word):
    """Edits a word in the CSV file respective to its difficulty

    Args:
        word (str): The word to be edited
        new_word (str): The new word to replace the old word
    """
    # Sets a flag to indicate that the word is not found
    word_found = False
    # Initialize an empty list to store the rows of the CSV file
    rows = []
    # Convert the word to be edited to lowercase
    word = word.lower()
    if difficulty == "Simple":
        with open('words.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Convert the word in the row to lowercase
                word_in_row = row[0].lower()
                # If the word in the row is equal to the word to be edited, set word_found to True and edit the word
                if word_in_row == word:
                    word_found = True
                    row[0] = new_word
                    # Append the edited row to the rows list
                    rows.append(row)
                # If the word in the row is not equal to the word to be edited, append the row to the rows list
                else:
                    rows.append(row)
        # If the word to be edited was not found in the CSV file, print an error message and return
        if not word_found:
            print(f"{word} not found in the CSV file")
            return
        # Overwrite the CSV file with the edited rows
        with open('words.csv', 'w', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile)
            # Iterate over rows and write each row to the csv file
            for row in rows:
                writer.writerow(row)
    else:
        with open('ComplexWords.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Convert the word in the row to lowercase
                word_in_row = row[0].lower()
                # If the word in the row is equal to the word to be edited, set word_found to True and edit the word
                if word_in_row == word:
                    word_found = True
                    row[0] = new_word
                    # Append the edited row to the rows list
                    rows.append(row)
                # If the word in the row is not equal to the word to be edited, append the row to the rows list
                else:
                    rows.append(row)
        # If the word to be edited was not found in the CSV file, print an error message and return
        if not word_found:
            print(f"{word} not found in the CSV file")
            return
        # Overwrite the CSV file with the edited rows
        with open('ComplexWords.csv', 'w', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile)
            # Iterate over rows and write each row to the csv file
            for row in rows:
                writer.writerow(row)


def edit_meaning_in_csv(word, new_meaning):
    """Edit the meaning of a word in a CSV file

    Args:
        word (str): The word whose meaning is to be edited
        new_meaning (str): The new meaning of the word
    """
    # Sets a flag to indicate that the word is not found
    word_found = False
    # Initialize an empty list to store the rows of the CSV file
    rows = []
    # Convert the word to be edited to lowercase
    word = word.lower()
    # Open the CSV file in read mode
    if difficulty == "Simple":
        with open('words.csv', 'r', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)
            # Iterate over rows in the CSV file
            for row in reader:
                # Convert the word in the row to lowercase
                word_in_row = row[0].lower()
                # If the word in the row is equal to the word to be edited, set word_found to True and edit the meaning
                if word_in_row == word:
                    word_found = True
                    row[1] = new_meaning
                    # Append the edited row to the rows list
                    rows.append(row)
                # If the word in the row is not equal to the word to be edited, append the row to the rows list
                else:
                    rows.append(row)
        # If the word to be edited was not found in the CSV file, print an error message and return
        if not word_found:
            print(f"{word} not found in the CSV file")
            return
        # Open the CSV file in write mode
        with open('words.csv', 'w', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile)
            # Iterate over rows and write each row to the csv file
            for row in rows:
                writer.writerow(row)
    else:
        with open('ComplexWords.csv', 'r', newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.reader(csvfile)
            # Iterate over rows in the CSV file
            for row in reader:
                # Convert the word in the row to lowercase
                word_in_row = row[0].lower()
                # If the word in the row is equal to the word to be edited, set word_found to True and edit the meaning
                if word_in_row == word:
                    word_found = True
                    row[1] = new_meaning
                    # Append the edited row to the rows list
                    rows.append(row)
                # If the word in the row is not equal to the word to be edited, append the row to the rows list
                else:
                    rows.append(row)
        # If the word to be edited was not found in the CSV file, print an error message and return
        if not word_found:
            print(f"{word} not found in the CSV file")
            return
        # Open the CSV file in write mode
        with open('ComplexWords.csv', 'w', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile)
            # Iterate over rows and write each row to the csv file
            for row in rows:
                writer.writerow(row)


def configure_attempts():
    """Prompts the user to enter the number of attempts for each game, and updates the game configuration in the game_setting.csv file
    """
    # Initialize an empty dictionary to store the game configuration
    config = {}
    # Open the game_setting.csv file in read mode
    with open('game_setting.csv', 'r') as game_setting_file:
        # Create a CSV reader object
        reader = csv.reader(game_setting_file)
        # Read the headers of the CSV file
        headers = next(reader)
        # Iterate over the rows of the CSV file and store the configuration values in the config dictionary
        for row in reader:
            config['Attempts'] = int(row[0])
            config['Words_per_attempt'] = int(row[1])
            config['player_output'] = int(row[2])
            config['password'] = row[3]
            config['difficulty'] = row[4]
    # Loop until the user enters a valid number of attempts or quits the program
    while True:
        # Prompt the user to enter the number of attempts
        attempts_str = input(
            "Enter the number of attempts for each game (or 'quit' to exit): ")
        # If the user enters 'quit', break out of the loop
        if attempts_str.lower() == 'quit':
            break
        try:
            # Try to convert the user's input to an integer
            attempts = int(attempts_str)
            # If the number of attempts is less than or equal to 0, print an error message
            if attempts <= 0:
                print("Please enter a positive integer")
            # If the number of attempts is valid, update the config dictionary and break out of the loop
            else:
                config['Attempts'] = attempts
                break
        except ValueError:
            print("Please enter a valid integer")
    # Open the game_setting.csv file in write mode
    with open('game_setting.csv', 'w', newline='') as game_setting_file:
        writer = csv.writer(game_setting_file)
        # Write the headers row to the csv file
        writer.writerow(headers)
        # Write the updated number of attempts, words per attempt, player output, and password to the csv file
        writer.writerow([config['Attempts'], config['Words_per_attempt'],
                        config['player_output'], config['password'], config['difficulty']])


def configure_words_per_attempt():
    """Prompts the user to enter the number of words per attempt for each game, and updates the game configuration in the game_setting.csv file
    """
    # Initialize an empty dictionary to store the config values
    config = {}
    # Open the game_setting.csv file in read mode
    with open('game_setting.csv', 'r') as game_setting_file:
        # Create a CSV reader object
        reader = csv.reader(game_setting_file)
        # Get the headers of the CSV file
        headers = next(reader)
        # Iterate over the rows of the CSV file and store the values in the config dictionary
        for row in reader:
            config['Attempts'] = int(row[0])
            config['Words_per_attempt'] = int(row[1])
            config['player_output'] = int(row[2])
            config['password'] = row[3]
            config['difficulty'] = row[4]
    # Keep prompting the user for the number of words per attempt until a valid input is provided
    while True:
        # Get the user's input
        words_per_attempts_str = input(
            "Enter the number of words per attempt (or 'quit' to exit): ")
        # If the user wants to exit, break out of the loop
        if words_per_attempts_str.lower() == 'quit':
            break
        try:
            # Try to convert the user's input to an integer
            words_per_attempts = int(words_per_attempts_str)
            # If the number of words per attempt is less than or equal to zero, print an error message
            if words_per_attempts <= 0:
                print("Please enter a positive integer")
            # If the number of words per attempt is valid, update the config dictionary and break out of the loop
            else:
                config['Words_per_attempt'] = words_per_attempts
                break
        # If the user's input cannot be converted to an integer, print an error message
        except ValueError:
            print("Please enter a valid integer")
    # Open the game_setting.csv file in write mode
    with open('game_setting.csv', 'w', newline='') as game_setting_file:
        # Create a CSV writer object
        writer = csv.writer(game_setting_file)
        # Write the headers to the CSV file
        writer.writerow(headers)
        # Write the updated config values to the CSV file
        writer.writerow([config['Attempts'], config['Words_per_attempt'],
                        config['player_output'], config['password'], config['difficulty']])


def change_player_output():
    """Prompts the user to enter the number of players to display after the game ends, and updates the game configuration in the game_setting.csv file
    """
    # Initialize an empty dictionary to store the configuration settings
    config = {}
    # Open the game setting CSV file in read mode
    with open('game_setting.csv', 'r') as game_setting_file:
        # Create a CSV reader object
        reader = csv.reader(game_setting_file)
        # Store the headers in a separate variable
        headers = next(reader)
        # Iterate over the rows and store the values in the config dictionary
        for row in reader:
            config['Attempts'] = int(row[0])
            config['Words_per_attempt'] = int(row[1])
            config['player_output'] = int(row[2])
            config['password'] = row[3]
            config['difficulty'] = row[4]
    # Keep prompting the user for input until a valid input is entered
    while True:
        # Get the number of players to be displayed after the game ends from the user
        player_output_str = input(
            "Enter how many players should be displayed after the game ends (or 'quit' to exit): ")
        # If the user entered 'quit', break out of the loop
        if player_output_str.lower() == 'quit':
            break
        # Try to convert the input to an integer
        try:
            player_output = int(player_output_str)
            # If the input is not a positive integer, print an error message
            if player_output <= 0:
                print("Please enter a positive integer")
            # If the input is a valid integer, update the config dictionary and break out of the loop
            else:
                config['player_output'] = player_output
                break
        # If the input cannot be converted to an integer, print an error message
        except ValueError:
            print("Please enter a valid integer")
    # Open the game setting CSV file in write mode
    with open('game_setting.csv', 'w', newline='') as game_setting_file:
        # Create a CSV writer object
        writer = csv.writer(game_setting_file)
        # Write the headers to the CSV file
        writer.writerow(headers)
        # Write the updated configuration settings to the CSV file
        writer.writerow([config['Attempts'], config['Words_per_attempt'],
                        config['player_output'], config['password'], config['difficulty']])


def change_password():
    """
    Prompts the user to enter the current password and, if it is correct, prompts the user to enter a new password.
    The new password must contain at least one digit, one uppercase and one lowercase character, and one of the following
    special symbols: !@#$%. The password must also be between 4 and 20 characters long. If the user successfully changes
    the password, the new password is saved to the 'game_setting.csv' file.
    """
    while True:
        checkPass = getpass.getpass(
            prompt=("Please enter the current password (or press 'quit' to exit): "))
        with open('game_setting.csv', 'r', newline='') as game_setting_file:
            rows = list(csv.reader(game_setting_file))
        correct_password = rows[1][3]
        if checkPass == correct_password:
            while True:
                # Prompts the user to get the new password
                new_password = input(
                    "Enter a new password (or 'quit' to exit): ")
                # If the user entered 'quit', break out of the loop
                if new_password.lower() == 'quit':
                    break
                # Check if the password contains at least one digit
                if any(char.isdigit() for char in new_password):
                    # Check if the password contains at least one uppercase and one lowercase character
                    if any(char.isupper() for char in new_password) and any(char.islower() for char in new_password):
                        # Check if the password contains at least one special symbol
                        if any(char in "!@#$%" for char in new_password):
                            # Check if the password is between 4 and 20 characters long
                            if 4 <= len(new_password) <= 20:
                                # Open the game_setting.csv file in read mode
                                with open('game_setting.csv', 'r', newline='') as game_setting_file:
                                    # Convert the file object to a list of rows
                                    rows = list(csv.reader(game_setting_file))
                                # Edit the password in the second row (index 1) of the rows list
                                rows[1][3] = new_password
                                # Open the game_setting.csv file in write mode
                                with open('game_setting.csv', 'w', newline='') as game_setting_file:
                                    # Create a CSV writer object
                                    writer = csv.writer(game_setting_file)
                                    # Write all rows to the game_setting.csv file
                                    writer.writerows(rows)
                                print("Password changed successfully")
                                break
                            else:
                                print(
                                    "Password must be between 4 to 20 characters long")
                        else:
                            print(
                                "Password must contain at least one of these special symbols: !@#$%")
                    else:
                        print(
                            "Password must contain at least one uppercase and one lowercase character")
                else:
                    print("Password must contain at least one number")
            break
        elif checkPass.lower() == "quit":
            break
        else:
            print("Invalid password.")


def display_top_players():
    """The top players are displayed in groups of five, with the option to view the next or previous group of players or quit the program.
    """
    # Read the scores from the CSV file and store them in a list
    scores = []
    with open('scores.csv', 'r', newline='') as scores_file:
        reader = csv.reader(scores_file)
        # Skip the headers row
        next(reader)
        for row in reader:
            username = row[0]
            score = row[1]
            # Try to convert the score to an integer
            try:
                score = int(score)
            # If the score is not a valid integer, skip this row
            except ValueError:
                continue
            # Append the username and score to the scores list
            scores.append([username, score])
    # Sort the scores list in descending order by score
    scores.sort(key=lambda x: x[1], reverse=True)

    # Set the number of players to display at a time
    num_players = 5
    # Initialize the start index for the players to display
    start_index = 0

    # Keep looping until the user quits
    while start_index < len(scores):
        # Print the top players
        print("Top Players:")
        # Iterate over the players to display
        for i in range(start_index, start_index + num_players):
            # If the index is out of range, break the loop
            if i >= len(scores):
                break
            # Print the player's rank, username, and score
            print(f"{i+1}. {scores[i][0]}: {scores[i][1]}")
        # Prompt the user to see the next set of players, the previous set of players, or quit
        user_input = input(
            "Press 'n' to see the next set of players, 'b' to see the previous set of players, or 'q' to quit: ")
        # If the user wants to see the next set of players, increase the start index by the number of players to display
        if user_input.lower() == 'n':
            start_index += num_players
            # If the start index is out of range, set it to the last possible index
            if start_index >= len(scores):
                start_index = len(scores) - num_players
        # If the user wants to see the previous set of players, decrease the start index by the number of players to display
        elif user_input.lower() == 'b':
            start_index -= num_players
            if start_index < 0:
                start_index = 0
        # If the user presses "q", the loop is broken and the function ends.
        elif user_input.lower() == 'q':
            break


def update_difficulty():
    """Updates the difficulty level in the CSV file game_setting.csv
    Prompts the user to input either 1 for Simple difficulty or 2 for Complex difficulty
    If the user inputs 'quit', the function breaks
    """
    while True:
        getDifficulty = input(
            "Enter the difficulty level, 1 = Simple 2 = Complex (or press 'quit' to exit): ")
        if getDifficulty.lower() == 'quit':
            break
        if getDifficulty == "1":
            getDifficulty = "Simple"
            # Open game_setting.csv in read mode, convert the content to a list of rows
            with open('game_setting.csv', 'r', newline='') as game_setting_file:
                rows = list(csv.reader(game_setting_file))
            # Update the difficulty level in the second row (index 1)
            rows[1][4] = getDifficulty
            # Open game_setting.csv in write mode, write the modified rows to the file
            with open('game_setting.csv', 'w', newline='') as game_setting_file:
                writer = csv.writer(game_setting_file)
                writer.writerows(rows)
            break
        elif getDifficulty == "2":
            getDifficulty = "Complex"
            # Open game_setting.csv in read mode, convert the content to a list of rows
            with open('game_setting.csv', 'r', newline='') as game_setting_file:
                rows = list(csv.reader(game_setting_file))
            # Update the difficulty level in the second row (index 1)
            rows[1][4] = getDifficulty
            # Open game_setting.csv in write mode, write the modified rows to the file
            with open('game_setting.csv', 'w', newline='') as game_setting_file:
                writer = csv.writer(game_setting_file)
                writer.writerows(rows)
            break
        else:
            print("Invalid input. Please try again.")


def admin_login():
    """
    Prompt the user to enter a username and password, and check if the password matches the
    password stored in the game_setting.csv file. If the login is successful, the sub_menu function is called.
    The function continues to loop until the user enters 'quit' to exit.
    """
    # Loops infinitely until it breaks
    while True:
        # Prompts the user for a username
        username = input("Enter a username (or 'quit' to exit): ")
        # If the user inputs quit, the loop will break
        if username.lower() == 'quit':
            break
        elif username == "admin":
            while True:
                # Prompts the user for a password that will be hidden by getpass
                password = getpass.getpass(
                    prompt="Enter a password (or 'quit' to exit): ")
                # if the user inputs quit, the loop will break
                if password.lower() == 'quit':
                    break
                with open('game_setting.csv', 'r', newline='') as game_setting_file:
                    rows = list(csv.reader(game_setting_file))
                correct_password = rows[1][3]
                if password == correct_password:
                    print("Login successful\n----------------")
                    sub_menu()
                    break
                else:
                    print("Invalid password")
                    break
        else:
            print("No such user.")


def main_menu():
    """This function presents the main menu options to the user and allows them to choose one of three options
    If the user inputs a number that is not valid, they are prompted to enter a valid option unless they choose to quit
    """
    # Gets the user input to decide which function to call
    main_menu_option = input(
        "1. Show current leaderboard\n2. Edit game settings\n3. Quit\n>> ")
    # Checks if the input is numeric (0-9)
    if main_menu_option.isnumeric():
        # Converts the input into an integer
        main_menu_option = int(main_menu_option)
        if main_menu_option == 1:
            # Displays the current leaderboard
            display_top_players()
            main_menu()
        elif main_menu_option == 2:
            # Login menu for admin config
            admin_login()
            main_menu()
        elif main_menu_option == 3:
            # Exits the menu
            exit()
        else:
            print("Please enter a valid option")
            main_menu()
    else:
        print("Please enter a valid option")
        main_menu()


def sub_menu():
    """Display the sub menu options for the admin user and calls the respective functions    
    """
    # Gets the user input to decide which function to call
    sub_menu_option = input(
        "1. Add a word\n2. Delete a word\n3. Edit a word\n4. Edit a meaning\n5. Edit game settings\n6. Back\n>> ")
    # Checks if the input is numeric (0-9)
    if sub_menu_option.isnumeric():
        # Converts the input into an integer
        sub_menu_option = int(sub_menu_option)
        if sub_menu_option == 1:
            while True:
                # Prompts the user to get a word
                word = input(
                    "Please choose a word to add (or 'quit' to exit): ")
                if word == "quit":
                    sub_menu()
                elif word.isalpha():
                    # Prompts the user to get a meaning
                    meaning = input("Please give a meaning of the word: ")
                    # Calls the function with the arguments word and meaning passed into the function
                    add_into_csv(word, meaning)
                    sub_menu()
                else:
                    print("Please enter a word that consists of only alphabets")
        elif sub_menu_option == 2:
            while True:
                # Prompts the user to get a word
                word = input(
                    "Enter the word to remove (or 'quit' to exit): ").lower()
                if word == "quit":
                    sub_menu()
                elif word.isalpha():
                    # Calls the function with the argument word passed into the function
                    delete_from_csv(word)
                    sub_menu()
                else:
                    print("Please enter a word that only consists of alphabets")

        elif sub_menu_option == 3:
            while True:
                # Prompts the user to get a word
                word = input(
                    "Enter the word you wish to rename (or 'quit' to exit): ")
                if word == "quit":
                    sub_menu()
                elif word.isalpha():
                    # Prompts the user to rename the word
                    new_word = input("Enter the new name: ")
                    edit_word_from_csv(word, new_word)
                    sub_menu()
                else:
                    print("Please enter a word that only consists of alphabets")

        elif sub_menu_option == 4:
            while True:
                # Prompts the user to get a word
                word = input(
                    "Enter the word you wish to change the meaning of (or 'quit' to exit): ")
                if word == "quit":
                    sub_menu()
                elif word.isalpha():
                    # Prompts the user to get the meaning of the word
                    new_meaning = input("Enter the new meaning: ")
                    edit_meaning_in_csv(word, new_meaning)
                    sub_menu()
                else:
                    print("Please enter a word that only consists of alphabets")

        elif sub_menu_option == 5:
            # Enters the submenu
            sub_sub_menu()
            sub_menu()
        elif sub_menu_option == 6:
            # Go back
            main_menu()
        else:
            print("Please enter a valid option")
            sub_menu()
    else:
        print("Please enter a valid option")
        sub_menu()


def sub_sub_menu():
    """Display the sub sub menu options for the admin user and calls the respective functions    
    """
    # Gets the user input to decide which function to call
    sub_sub_menu_option = input(
        "1. Configure game difficulty\n2. Configure number of attempts\n3. Configure number of words per attempt\n4. Configure Leaderboard output\n5. Change admin password\n6. Back\n>> ")
    if sub_sub_menu_option.isnumeric():
        sub_sub_menu_option = int(sub_sub_menu_option)
        if sub_sub_menu_option == 1:
            update_difficulty()
            sub_sub_menu()
        elif sub_sub_menu_option == 2:
            configure_attempts()
            sub_sub_menu()
        elif sub_sub_menu_option == 3:
            configure_words_per_attempt()
            sub_sub_menu()
        elif sub_sub_menu_option == 4:
            change_player_output()
            sub_sub_menu()
        elif sub_sub_menu_option == 5:
            change_password()
            sub_sub_menu()
        elif sub_sub_menu_option == 6:
            sub_menu()
    else:
        print("Please enter a valid option")
        sub_sub_menu()


main_menu()
