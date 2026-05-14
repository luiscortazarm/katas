import pytest
from kata1 import Dictionary


def test_dictionary_entries():
    d = Dictionary()
    d.newentry('Apple', 'A fruit that grows on trees')

    # Added word can be recovered
    assert d.look('Apple') == 'A fruit that grows on trees'

    # Inexistent word returns a warning
    assert d.look('Banana') == "Can't find entry for Banana"
