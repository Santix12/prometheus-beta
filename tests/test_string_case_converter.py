import pytest
from src.string_case_converter import convert_to_alternating_dot_case

def test_basic_string_conversion():
    assert convert_to_alternating_dot_case("hello") == 'h.e.l.l.o'
    assert convert_to_alternating_dot_case("world") == 'w.o.r.l.d'

def test_multiple_word_string():
    assert convert_to_alternating_dot_case("hello world") == 'h.e.l.l.o. .w.o.r.l.d'

def test_empty_string():
    assert convert_to_alternating_dot_case("") == ''

def test_mixed_case_string():
    assert convert_to_alternating_dot_case("PYTHON") == 'P.y.T.h.O.n'
    assert convert_to_alternating_dot_case("PythonProgramming") == 'P.y.T.h.O.n.P.r.O.g.R.a.M.m.I.n.G'

def test_string_with_special_characters():
    assert convert_to_alternating_dot_case("hello-world!") == 'h.e.l.l.o.-.w.o.r.l.d.!'

def test_invalid_input_type():
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(12345)
    
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(None)

def test_single_character_string():
    assert convert_to_alternating_dot_case("a") == 'a'
    assert convert_to_alternating_dot_case("Z") == 'Z'