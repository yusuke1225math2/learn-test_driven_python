def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true", help="some boolean option")
    parser.addoption("--foo", action="store", help="foo: bar or baz")
