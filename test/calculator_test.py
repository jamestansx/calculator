from basic_calculator import *

input = [1, 2, 3, 4]
edge_input = [2, 3, 4, 5]


def test_add():

    assert add(input) == 1 + 2 + 3 + 4


def test_sub():

    assert sub(input) == 1 - 2 - 3 - 4


def test_mul():

    assert mul(input) == 1 * 2 * 3 * 4


def test_mul_edges():

    assert mul(edge_input) == 2 * 3 * 4 * 5


def test_div():

    assert div(input) == 1 / 2 / 3 / 4
