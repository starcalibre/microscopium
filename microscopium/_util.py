import numpy as np
import numbers


def groupby(key, iterable, transform=None):
    """Group items in `iterable` in a dictionary according to `key`.

    Parameters
    ----------
    key : function
        Returns a hashable when given an item in `iterable`.
    iterable : tuple, list, generator, or array-like
        The items to be grouped.
    transform : function, optional
        Transform the items before grouping them.

    Returns
    -------
    grouped : dict
        A dictionary mapping keys to elements of iterable. This has
        the form:
            ``{key(elem): [transform(elem)] for elem in iterable}``

    Examples
    --------
    >>> g = groupby(lambda x: x % 2, range(6), lambda x: x ** 2)
    >>> sorted(g.keys())
    [0, 1]
    >>> g[0]
    [0, 4, 16]
    >>> g[1]
    [1, 9, 25]
    """
    if transform is None:
        transform = lambda x: x
    grouped = {}
    for elem in iterable:
        grouped.setdefault(key(elem), []).append(transform(elem))
    return grouped


def normalise_random_state(seed):
    """Turn seed into a numpy RandomState instance.

    Parameters
    ----------
    seed : None, int, or numpy RandomState instance
        The input seed/random state.

    Returns
    -------
    random : numpy RandomState instance.
        The resulting RandomState instance.

    Notes
    -----
    This function is copied almost verbatim from scikit-learn's
    ``sklearn.utils.validation.check_random_state``, and so is
    governed by that library's code license (New BSD at the time of
    this writing.)
    """
    if seed is None:
        return np.random.mtrand._rand
    if isinstance(seed, (numbers.Integral, np.integer)):
        return np.random.RandomState(seed)
    if isinstance(seed, np.random.RandomState):
        return seed
    else:
        raise ValueError('Invalid input %s to generate random state' % seed)


def int_or_none(n):
    """Returns input n cast as int, or None if input is none.

    This is used in parsing sample information from image filenames.

    Parameters
    ----------
    n : any value castable as int, None
        The input value.

    Returns
    -------
    The input value cast an int, or None.

    Examples
    --------
    >>> int_or_none(3.0)
    3
    >>> int_or_none(None)
    """
    return int(n) if n is not None else None
