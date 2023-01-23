import sys
from verbecc import Conjugator

french_test_list = []
english_test_list = []


def select_language():
    languages = {
        "1": {"code": "fr", "language": "French"},
        "2": {"code": "es", "language": "Spanish"},
    }

    print("Select a target language")
    for key in languages.keys():
        print(f'{key} - {languages[key]["language"]}')

    while True:
        language = input("--> ")
        try:
            language = languages[language]["code"]
            break
        except KeyError:
            print(
                "Enter a valid number from the list to choose a language or 0 to exit"
            )
            if language == "0":
                sys.exit(0)

    cg = Conjugator(lang=language)
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


def display_and_get_mood(conjugation_list):
    moods = conjugation_list["moods"].keys()
    for index, mood in enumerate(moods):
        print(f"{index +1 } - {mood}")

    selected_moods = input("Select the mood(s) to practice, separated by a space --> ")
    selected_moods = selected_moods.split(" ")
    return selected_moods


def validate_selected_mood(selected_moods, conjugation_list):
    bad_entries, good_entries = [], []
    mood_list = list(conjugation_list["moods"])
    correct_numbers = range(len(mood_list))

    for mood in selected_moods:
        index = int(mood) - 1  # TODO: is this transparent, do outside function?
        if index in correct_numbers:
            good_entries.append(mood_list[index])
        else:
            bad_entries.append(mood_list[index])

    print(good_entries)  # remove
    if bad_entries:
        print(f"\nThe following are not valid entries {bad_entries}")
    return good_entries


def validate_selected_tense(selected_mood_and_tense, conjugation_list):
    pass


def display_and_get_tense(mood_names, conjugation_list):
    selected_mood_and_tense = {}
    bad_entries = []

    for mood_name in mood_names:
        tenses = list(conjugation_list["moods"][mood_name].keys())

        for index, tense in enumerate(tenses):
            print(f"{index  } - {tense}")

        selected_tenses = input(
            f"\nSelect the tense(s) to practice for {mood_name}, separated by a space --> "
        )
        selected_tenses = selected_tenses.split(" ")

        # validation of input for tense
        tense_names = []
        for index, tense in enumerate(selected_tenses):
            try:
                if (tense.isdigit()) and (int(tense) <= len(selected_tenses)):
                    tense_names.append(tenses[index])
                    continue
            except ValueError:
                pass

            bad_entries.append(tense)

        # build dictionary
        selected_mood_and_tense[mood_name] = tense_names

        if bad_entries:
            print(f"\nThe following are not valid entries {bad_entries}")
        print(selected_mood_and_tense)
    return selected_mood_and_tense


def drill_and_practice(selected_mood_and_tense, conjugation_list):
    for mood in selected_mood_and_tense.keys():
        print(mood)
        tenses = selected_mood_and_tense[mood]
        print(tenses)


def sanitize_data(verb):
    verb = verb.strip().replace(" ", "").lower()
    return verb


def check_user_input(answer, index):
    "Check if the user entered the correct/expected conjugation"
    return sanitize_data(answer) == sanitize_data(french_test_list[index])


def get_user_input():
    pass


def display_question():
    "Display the verb conjugation the user has to enter"
    print("Conjugate in french the verb {test_verb}")

    for index, verb in enumerate(english_test_list):
        print(f"{verb} ", end="")
        reply = get_user_input()
        if check_user_input(reply, index):
            print("Correct")
        else:
            print(f"Sorry the answer is {french_test_list[index]}")


def display_full_verb_conjugation():
    "Display the entire conjugation list for the verb (single tense)"

    for index, verb in enumerate(english_test_list):
        print(f"{verb} --> {french_test_list[index]}")


def display_menu():
    print("Select an option:")
    print("1 - Conjugated verb list ")
    print("2 - Drill and Practice")
    print("3 - Exit")
    print("--> ", end="")
    selection = input()
    return selection


def main():
    lang = select_language()
    conjugation_list = select_single_verb(lang)
    selected_moods = display_and_get_mood(conjugation_list)
    mood_names = validate_selected_mood(selected_moods, conjugation_list)
    mood_and_tense = display_and_get_tense(mood_names, conjugation_list)
    drill_and_practice(mood_and_tense, conjugation_list)


if __name__ == "__main__":
    main()
