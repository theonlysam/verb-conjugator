import sys

from verbecc import Conjugator


def display_language():
    languages = {
        "1": {"code": "fr", "language": "French"},
        "2": {"code": "es", "language": "Spanish"},
    }
    print("Select a target language")
    for key in languages.keys():
        print(f'{key} - {languages[key]["language"]}')
    return languages


def get_user_input(prompt="--> "):
    user_input = input(prompt)
    return user_input


def get_language_code(language, languages):
    try:
        language = languages[language]["code"]
    except KeyError:
        print("Enter a valid number from the list to choose a language or 0 to exit")
        if language == "0":
            sys.exit(0)
    return language


def get_language_instance(lang_code):
    cg = Conjugator(lang=lang_code)
    return cg


def select_single_verb(cg):
    error = False
    try:
        verb = input("Enter the verb to practice conjugating --> ")
    except AttributeError:
        print(f"Unable to find {verb} or it does not exist")
        error = True

    if not error:
        conjugation_list = cg.conjugate(verb)
        return conjugation_list


def display_mood(conjugation_list):
    moods = conjugation_list["moods"].keys()
    for index, mood in enumerate(moods):
        print(f"{index +1 } - {mood}")


# def split_entries(selected_entries):
#     selected_entries = selected_entries.split()
#     return selected_entries


def validate_selected_mood(selected_moods, conjugation_list):
    entries_list = list(conjugation_list["moods"])
    good_entries, bad_entries = validator(selected_moods, entries_list)

    if bad_entries:
        print(f"\nThe following are not valid entries {bad_entries}")
    return good_entries


def validate_selected_tense(mood, selected_tenses, conjugation_list):
    selected_mood_and_tense = {}
    tenses = list(conjugation_list["moods"][mood])
    good_entries, bad_entries = validator(selected_tenses, tenses)
    selected_mood_and_tense[mood] = good_entries

    if bad_entries:
        print(f"\nThe following are not valid entries {bad_entries}")
    return selected_mood_and_tense


def select_tense(selected_moods, conjugations):
    mood_tense_dict = {}
    for mood in selected_moods:
        display_tense(mood, conjugations)
        tense_list = get_user_input(
            prompt="Select the tense(s) to practice, separated by a space --> "
        )
        tense_list = tense_list.split()
        validated_tenses = validate_selected_tense(mood, tense_list, conjugations)
        mood_tense_dict.update(validated_tenses)
    print(mood_tense_dict)

    return mood_tense_dict


def display_tense(mood_name, conjugation_list):
    tenses = list(conjugation_list["moods"][mood_name].keys())
    print(tenses)
    for index, tense in enumerate(tenses):
        print(f"{index + 1 } - {tense}")


def validator(entries, item_list):
    bad_entries, good_entries = [], []
    correct_numbers = range(len(item_list))
    index = -1
    for entry in entries:
        try:
            index = int(entry) - 1
        except ValueError:
            pass
        if index in correct_numbers:
            good_entries.append(item_list[index])
        else:
            bad_entries.append(entry)
    return good_entries, bad_entries


def user_conjugation(selected_mood_and_tense, conjugation_list):

    for mood in selected_mood_and_tense.keys():
        tenses = selected_mood_and_tense[mood]
        for tense in tenses:
            print(f"\nConjugate the {tense} tense in the {mood} mood")
            conjugated_pronouns = conjugation_list["moods"][mood][tense]
            for pronoun in conjugated_pronouns:
                split_pronoun = pronoun.split()
                answer = get_user_input(prompt=f"-->{split_pronoun[0]} ")
                answer = answer.strip()
                answer = f"{split_pronoun[0]} {answer}"
                split_pronoun = f"{split_pronoun[0]} {split_pronoun[1]}"

                check_user_input(
                    sanitize_data(answer), sanitize_data(split_pronoun), pronoun
                )


def sanitize_data(verb):
    verb = verb.strip().replace(" ", "").lower()
    return verb


def check_user_input(user_answer, correct_answer, pronoun):
    "Check if the user entered the correct/expected conjugation"
    if sanitize_data(user_answer) == sanitize_data(correct_answer):
        print("Correct")
    else:
        print(f"Sorry the answer is {pronoun}")


def initiation_functions():
    languages = display_language()
    lang = get_user_input()
    lang_code = get_language_code(lang, languages)
    lang_instance = Conjugator(lang=lang_code)  # get_language_instance(lang_code)
    conjugation_list = select_single_verb(lang_instance)
    display_mood(conjugation_list)
    mood_list = get_user_input(prompt="Select the mood(s) separated by a space --> ")
    mood_list = mood_list.split()
    mood_names = validate_selected_mood(mood_list, conjugation_list)
    mood_tense_dict = select_tense(mood_names, conjugation_list)
    return mood_tense_dict, conjugation_list


def drill_and_practice():
    mood_tense_dict, conjugation_list = initiation_functions()

    while True:
        user_conjugation(mood_tense_dict, conjugation_list)
        try:
            user_repeat = input(
                "Do you want to practice this one again? 1-Yes, 2-No --> "
            )
        except ValueError:
            print("Invalid entry")
        if user_repeat == "1":
            continue
        elif user_repeat == "2":
            break


def display_verb_conjugation():
    "Displays the conjugation of the verb in the selected mood and tense"
    mood_tense_dict, conjugation_list = initiation_functions()

    for mood, tenses in mood_tense_dict.items():
        for tense in tenses:
            print(f"\n{mood} - {tense} tense")
            conjugated_pronouns = conjugation_list["moods"][mood][tense]
            for pronoun in conjugated_pronouns:
                print(pronoun)


def display_menu():
    print("\nSelect an option:")
    print("1 - Display verb conjugation ")
    print("2 - Drill and Practice")
    print("3 - Exit")
    selection = input("--> ")
    return selection


def main():
    while True:
        user_selection = display_menu()
        if user_selection == "1":
            display_verb_conjugation()
        elif user_selection == "2":
            drill_and_practice()
        else:
            print("\nGoodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()

