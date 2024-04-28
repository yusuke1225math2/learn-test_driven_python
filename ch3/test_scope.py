import pytest

@pytest.fixture(scope='function')
def func_scope():
    """A function scope fixture."""

@pytest.fixture(scope='module')
def mod_scope():
    """A module scope fixture."""

@pytest.fixture(scope='session')
def sess_scope():
    """A session scope fixture."""

@pytest.fixture(scope='class')
def class_scope():
    """A class scope fixture."""

def test_1(sess_scope, mod_scope, func_scope):
    """Test using session, module, and function scope fixtures."""

def test_2(sess_scope, mod_scope, func_scope):
    """Demo is same as test_1."""

@pytest.mark.usefixtures('class_scope')
class TestSomething():
    """Demo uses of class scope fixture."""
    def test_3(self):
        """Test using a class scope fixture."""

    def test_4(self):
        """Again, this is the same as test_3."""
