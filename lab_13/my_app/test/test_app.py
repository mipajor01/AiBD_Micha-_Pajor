import pytest
from my_app import app

testdata = [
    ([5,4,1,2,8,2],[1, 2, 2, 4, 5, 8])
]

@pytest.mark.parametrize('list, expected_output', testdata)
def test_text_contain_word(list, expected_output):
    assert app.bubble_sort(list) == expected_output