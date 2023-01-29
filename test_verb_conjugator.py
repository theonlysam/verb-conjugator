import pytest

from verbecc import Conjugator
from verb_conjugator import VerbConjugator


@pytest.fixture #scope="function"/"session"
def verb_con():
    return VerbConjugator()


def test_empty_verb_conjugator_instance(verb_con):    
    assert verb_con.selected_lang == None


def test_correct_language_keys(verb_con):
    test_dict = {"1":"",
                "2":""}
    assert verb_con.languages.keys() == test_dict.keys()


def test_number_language_keys(verb_con):
    key_number = len(verb_con.languages.keys())
    assert key_number == 2


def test_user_input(verb_con):
    "Test user input method returns what was passed in"
    user_input = verb_con.get_user_input(user_input="1")
    assert user_input == "1"


def test_correct_language_code_french(verb_con):
    "Test if the correct language code returned when french is choosen"
    language = "1"
    lang_code = verb_con.get_language_code(language)
    assert lang_code == "fr"


def test_correct_language_code_spanish(verb_con):
    "Test if the correct language code returned when spanish is choosen"
    language = "2"
    lang_code = verb_con.get_language_code(language)
    assert lang_code == "es"


def test_incorrect_language_code_raises_exception(verb_con):
    "Test if the exception is raised when incorrect language option choosen"
    language = "99"    
    with pytest.raises(KeyError) as e_info:
        lang_code = verb_con.get_language_code(language)
    

def test_nonexistent_french_verb_raises_exception(verb_con):
    "Want to test select_single_verb method"
    pass


def test_if_valid_french_moods_are_returned(verb_con):
    selected_moods = [1, 2, 3, 4, 5 ,6 ]
    expected_moods = [  'infinitif', 
                        'indicatif', 
                        'conditionnel', 
                        'subjonctif', 
                        'imperatif', 
                        'participe',                         
                    ]
    verb = "aller"
    lang_code ="fr"
    conjugator_instance = Conjugator(lang_code)
    verb_con.conjugations = conjugator_instance.conjugate(verb)
    validated_moods = verb_con.validate_selected_mood(selected_moods)
    assert validated_moods == expected_moods


def test_if_invalid_moods_are_returned(verb_con):
    pass


def test_if_invalid_moods_not_returned(verb_con):
    pass


def test_validator_returns_correct_values(verb_con):
    bad_entries, good_entries = [], []
    entries = [1,2,'d',99,'bad',4]
    item_list = [1,2,3,4,5,6]
    expected_good_entries = [1,2,4]
    expected_bad_entries = ['d',99,'bad']
    good_entries, bad_entries = verb_con.validator(entries, item_list)
    assert good_entries == expected_good_entries 


def test_validator_returns_incorrect_values(verb_con):
    bad_entries, good_entries = [], []
    entries = [1,2,'d',99,'bad',4]
    item_list = [1,2,3,4,5,6]
    expected_good_entries = [1,2,4]
    expected_bad_entries = ['d',99,'bad']
    good_entries, bad_entries = verb_con.validator(entries, item_list)
    assert bad_entries == expected_bad_entries


def test_sanitize_data_returns_correct(verb_con):
    verb = " ALLER"
    assert verb_con.sanitize_data(verb) == "aller" 


def test_check_user_input_returns_true_for_correct_answer(verb_con):
    assert verb_con.check_user_input("je vais", "je vais", "je") == True 


def test_check_user_input_does_not_return_false_for_correct_answer(verb_con):
    assert verb_con.check_user_input("je vais", "je vais", "je") != False 


def test_check_user_input_returns_false_for_incorrect_answer(verb_con):
    assert verb_con.check_user_input("I go", "je vais", "je") == False 