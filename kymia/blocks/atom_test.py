import pytest

from .atom import Atom, AtomImmutableProperty

def test_atom_creation():
    a = Atom('C', 1)
    assert a.name == 'C'

def test_atom_readonly():
    a = Atom('C', 1)
    with pytest.raises(AtomImmutableProperty):
        a.name = 'B'
