"""
More about Pytest

Fixtures:
https://docs.pytest.org/en/latest/fixture.html


"""

from RTP_python_template.list_util import mean, split
import pytest
import numpy as np


mean_list = [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (range(1, 1000000), 1000000/2.0)
]


@pytest.mark.skip('Not now')
@pytest.mark.parametrize('num_list, expected_mean', mean_list)
def test_many(num_list, expected_mean):
    # assert mean(num_list) == expected_mean
    assert np.isclose(mean(num_list), expected_mean, 1e-3)


@pytest.mark.parametrize('x', [1, 2, 3])
@pytest.mark.parametrize('y', [4, 5, 6])
def test_combinations(x, y, num_list_3):
    pass


@pytest.fixture
def num_list_3():
    return [1, 2, 3, 4, 5]


def test_ints(num_list_3):
    # num_list_3 = [1, 2, 3, 4, 5]
    obs = mean(num_list_3)
    exp = 3
    assert obs == exp


def test_zero():
    num_list = [0, 2, 4, 6]
    obs = mean(num_list)
    exp = 3
    assert obs == exp


def test_double():
    # This one will fail in Python 2
    num_list = [1, 2, 3, 4]
    obs = mean(num_list)
    exp = 2.5
    assert obs == exp


def test_empty():
    with pytest.raises(ZeroDivisionError):
        mean([])


def test_long():
    big = 100000000
    obs = mean(range(1, big))
    exp = big/2.0
    assert obs == exp


@pytest.mark.skip
def test_complex():
    # given that complex numbers are an unordered field
    # the arithmetic mean of complex numbers is meaningless
    pytest.skip('Complex numbers')
    num_list = [2 + 3j, 3 + 4j, -32 - 2j]
    obs = mean(num_list)
    exp = NotImplemented
    assert obs == exp

def test_mean_wrong_type():
    with pytest.raises(TypeError):
        mean('not a list')

# ------- Testing Split --------- #

ex_lists = [
    ([1, 2, 3, 4, 5], 3, [1, 2, 3], [4, 5]),
    ([], 3, [], []),
    ([1], 1, [1], []),
    ([1], 2, [1], []),
    ([1, 2], 1, [1], [2])
]


@pytest.mark.parametrize('args', ex_lists)
def test_split(args):
    big_list, index, ex_list1, ex_list2 = args
    list1, list2 = split(big_list, index)

    assert list1 == ex_list1
    assert list2 == ex_list2

def test_split_index():
    num_list = [1, 2, 3, 4]
    with pytest.raises(TypeError):
        split(num_list, 'wrong index type')


def test_split_wrong_type():
    with pytest.raises(TypeError):
        split('not list', 4)

