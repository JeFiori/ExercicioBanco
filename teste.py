import pytest

def somar(a, b):
    return a + b


@pytest.mark.parametrize('a,b,resultado',[
    (1, 2, 3),
    (3, 4, 7),
    (7, 8, 15),
    (1, 5, 6),
])
def test_somar(a,b,resultado):
    assert somar(a,b) == resultado




