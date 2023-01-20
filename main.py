import sys
test_verb = "aller";

french_test_list = ["je vais","tu vas", 'il va', "elle va", "on va","nous allons", "vous allez", "ils vont", "elles vont"]
english_test_list = ["I go", "You go", "He goes", "She goes", "One goes", "We go", "You go", "They go (masc)", "They go (fem)"]

def get_user_input():
    'Prompt user to enter an answer'
    # print("--> ", end="")
    answer = input("--> ", end="")    
    return answer

def sanitize_data(verb):   
    verb = verb.strip().replace(" ","").lower()
    return verb

def check_user_input(answer,index):
    'Check if the user entered the correct/expected conjugation'
    return sanitize_data(answer) == sanitize_data(french_test_list[index])

def display_question():
    'Display the verb conjugation the user has to enter'
    print("Conjugate in french the verb {test_verb}")

    for index, verb in enumerate(english_test_list):
        print(f'{verb} ', end="")
        reply = get_user_input()
        if check_user_input(reply,index):
            print("Correct")
        else:
            print(f'Sorry the answer is {french_test_list[index]}')

def display_full_verb_conjugation():
    'Display the entire conjugation list for the verb (single tense)'

    for index, verb in enumerate(english_test_list):
        print(f'{verb} --> {french_test_list[index]}')

def display_menu():
    print("Select an option:")
    print("1 - Conjugated verb list ")
    print("2 - Drill and Practice")
    print("3 - Exit")
    print("--> ", end="")
    selection = input()
    return selection

def main():
    while True:
        selection = display_menu()
        if selection == '1':
            display_full_verb_conjugation()
        elif selection == '2':
            display_question()
        elif selection == '3':
            sys.exit("Goodbye")
        else:
            print(" Option not recognised, try again")


if __name__ == "__main__":
    main()