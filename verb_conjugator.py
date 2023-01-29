import sys

from verbecc import Conjugator


class VerbConjugator():

    def __init__(self):
        self.languages = {
            "1": {"code": "fr", "language": "French"},
            "2": {"code": "es", "language": "Spanish"},
        }
        self.user_input = None
        self.selected_lang = None
        self.lang_code = None
        self.conjugator_instance = None #used to be cg
        self.conjugations = None
        self.selected_mood_and_tense = {}
        self.moods = []
        self.mood_names = []
        self.mood_tense = {}

    def display_language(self):
        print("Select a target language")
        for key in self.languages.keys():
            print(f'{key} - {self.languages[key]["language"]}')
    
    def get_user_input(self,prompt="--> "):
        user_input = input(prompt)
        return user_input

    def get_language_code(self,language):
        try:
            lang_code = self.languages[language]["code"]
        except KeyError:
            print("Enter a valid number from the list to choose a language or 0 to exit")
            if lang_code == "0":
                sys.exit(0)
        return lang_code

    def get_language_instance(self): # need to pass language code
        self.conjugator_instance = Conjugator(lang=self.lang_code)
    
    def select_single_verb(self):
        error = False
        verb = None
        try:
            verb = input("Enter the verb to practice conjugating --> ")
        except AttributeError:
            print(f"Unable to find {verb} or it does not exist")
            error = True

        if not error:            
            return self.conjugator_instance.conjugate(verb)

    def display_mood(self):
        moods = self.conjugations["moods"].keys()
        for index, mood in enumerate(moods):
            print(f"{index +1 } - {mood}")     

    def validate_selected_mood(self, selected_moods):
        entries_list = list(self.conjugations["moods"])
        good_entries, bad_entries = self.validator(selected_moods, entries_list)
    
        if bad_entries:
            print(f"\nThe following are not valid entries {bad_entries}")
        return good_entries

    def validate_selected_tense(self, mood, selected_tenses):
        selected_mood_and_tense = {}
        tenses = list(self.conjugations["moods"][mood])
        good_entries, bad_entries = self.validator(selected_tenses, tenses)
        selected_mood_and_tense[mood] = good_entries

        if bad_entries:
            print(f"\nThe following are not valid entries {bad_entries}")
        return selected_mood_and_tense
        
    def select_tense(self, selected_moods):
        # import pdb; pdb.set_trace()
        mood_tense_dict = {}
        for mood in selected_moods:
            self.display_tense(mood)
            tense_list = self.get_user_input(
                prompt="Select the tense(s) to practice, separated by a space --> "
            )
            tense_list = tense_list.split()
            validated_tenses = self.validate_selected_tense(mood, tense_list)
            mood_tense_dict.update(validated_tenses)
        return mood_tense_dict

    def display_tense(self,mood_name):
        tenses = list(self.conjugations["moods"][mood_name].keys())        
        for index, tense in enumerate(tenses):
            print(f"{index + 1 } - {tense}")

    def validator(self, entries, item_list):
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
    
    def quiz_user(self):
    
        for mood in self.mood_tense.keys():
            tenses = self.mood_tense[mood]
            for tense in tenses:
                print(f"\nConjugate the {tense} tense in the {mood} mood")
                conjugated_pronouns = self.conjugations["moods"][mood][tense]
                for pronoun in conjugated_pronouns:
                    split_pronoun = pronoun.split()
                    answer = self.get_user_input(prompt=f"-->{split_pronoun[0]} ")
                    answer = answer.strip()
                    answer = f"{split_pronoun[0]} {answer}"
                    split_pronoun = f"{split_pronoun[0]} {split_pronoun[1]}"

                    self.check_user_input(
                        self.sanitize_data(answer), self.sanitize_data(split_pronoun), pronoun
                    )

    def sanitize_data(self, verb):
        verb = verb.strip().replace(" ", "").lower()
        return verb

    def check_user_input(self, user_answer, correct_answer, pronoun):
        "Check if the user entered the correct/expected conjugation"
        if self.sanitize_data(user_answer) == self.sanitize_data(correct_answer):
            print("Correct")
        else:
            print(f"Sorry the answer is {pronoun}")

    def drill_and_practice(self):
        # mood_tense_dict, conjugation_list = initiation_functions()

        while True:
            self.quiz_user()
            try:
                user_repeat = input(
                    "Do you want to practice this one again? 1-Yes, 2-No --> "
                )
            except ValueError:
                print("Invalid entry")
            if user_repeat == "1":
                continue
            else:
                break

    def display_verb_conjugation(self):
        "Displays the conjugation of the verb in the selected mood and tense"
        # mood_tense_dict, conjugation_list = initiation_functions()
        
        for mood, tenses in self.mood_tense.items():
            for tense in tenses:
                print(f"\n{mood} - {tense} tense")
                conjugated_pronouns = self.conjugations["moods"][mood][tense]
                for pronoun in conjugated_pronouns:
                    print(pronoun)

    def setup(self):
        self.display_language()
        self.selected_lang = self.get_user_input()
        self.lang_code = self.get_language_code(self.selected_lang)
        self.get_language_instance()
        self.conjugations = self.select_single_verb()
        self.display_mood()
        self.moods = self.get_user_input(prompt="Select the mood(s) separated by a space --> ")
        self.moods = self.moods.split()
        self.mood_names = self.validate_selected_mood(self.moods)
        self.mood_tense = self.select_tense(self.mood_names)

    def display_menu(self):
        print("\nSelect an option:")
        print("1 - Display verb conjugation ")
        print("2 - Drill and Practice")
        print("3 - Exit")
        selection = input("--> ")
        return selection


vc = VerbConjugator()
vc.setup()
vc.drill_and_practice()