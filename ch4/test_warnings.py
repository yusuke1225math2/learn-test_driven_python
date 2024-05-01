import warnings
import pytest

def lame_function():
    warnings.warn("Please stop using this", DeprecationWarning)
    # 関数の他の部分

def test_lame_function(recwarn):
    lame_function()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'

def test_lame_function_2():
    # with pytest.warns(None) as warning_list:
    # pytest.warns(None)は現在は非推奨になりました
    # https://github.com/scikit-learn/scikit-learn/issues/22572
    with warnings.catch_warnings(record=True) as warning_list:
        lame_function()

    assert len(warning_list) == 1
    w = warning_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'
