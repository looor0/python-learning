import pytest

@pytest.mark.parametrize("input_str, expected", [
    ("Hello", "olleH"), #test cases
    ("Apple", "elppA"),
    ("Python", "nohtyP"),
])
def test_reverse_string(input_str, expected):  #decorates
    assert input_str[::-1] == expected

import pytest

#when to have multiple inputs
@pytest.mark.parametrize("input_dict, expected", [
    ({'name': 'Apple', 'color': 'Red'}, 'Apple is Red'),
    ({'name': 'Banana', 'color': 'Yellow'}, 'Banana is Yellow'),
])
def test_fruit_description(input_dict, expected):
    fruit_desc = f"{input_dict['name']} is {input_dict['color']}"
    assert fruit_desc == expected
    
    
#external code need to run:
!pytest test_parameterized.py
