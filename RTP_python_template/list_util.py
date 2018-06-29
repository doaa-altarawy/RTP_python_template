"""
Contains some methods on lists
"""


def mean(num_list):
    """
    Calculates the mean of a list of numbers

    Parameters
    ----------
    num_list: list (int or float)


    Returns
    -------
    ret: int or float
        The mean of the list


    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    try:
        return sum(num_list)/len(num_list)
    except TypeError as err:
        msg = 'Input must be a list of int or float'
        raise TypeError(err.__str__() + '\n' + msg)
    except ZeroDivisionError as err:
        raise ZeroDivisionError(err)


def split(num_list, index):
    """
    Split a list into two from the given index
    """
    if not isinstance(num_list, list):
        raise TypeError('Split method takes a list, % is given'.format(type(num_list)))

    if not isinstance(index, int):
        raise TypeError('Index must be an Integer, % is given'.format(type(index)))

    list1 = num_list[:index]
    list2 = num_list[index:]

    return list1, list2
