from fixtures import *

def test_some_data(some_data):
    # проверяем, что функция вернула то, что должна вернуть
    assert some_data == 42
#py.test test_1.py