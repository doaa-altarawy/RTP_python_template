
def mean(num_list):
    """
    Claculate the mean of a sequence

    Parameters
    ----------
    num_list: sequence of int or float

    Returns
    -------
        mean of the sequence
    """

    return sum(num_list)/len(num_list)


def split(num_list, index):
    """
    Split a sequence into two from the given index
    """

    list1 = num_list[:index]
    list2 = num_list[index:]

    return list1, list2
