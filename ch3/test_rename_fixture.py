import pytest

@pytest.fixture(name='lue')
def ultimate_answer_to_life_the_universe_and_everything():
    """究極の答えを返す"""
    return 42

def test_everything(lue):
    assert lue == 42
