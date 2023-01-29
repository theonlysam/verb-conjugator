import sys

from verb_conjugator import VerbConjugator


def main():
    vc = VerbConjugator()    

    while True:
        user_selection = vc.display_menu()
        if user_selection == "1":
            vc.setup()
            vc.display_verb_conjugation()
        elif user_selection == "2":
            vc.setup()
            vc.drill_and_practice()
        else:
            print("\nGoodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()

