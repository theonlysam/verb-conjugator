import pytest

from verb_conjugator import VerbConjugator


@pytest.fixture #scope="function"/"session"
def verb_con():
    return VerbConjugator()

def test_empty_verb_conjugator_instance(verb_con):    
    assert verb_con.selected_lang == None