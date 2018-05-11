from .lang.sw import Number


def num_to_words(number, **kwargs):
    """Get number in words.

    Args:
        number (int): a numerical value to be converted.

        kwargs: a optional keyword arguments
            use_lakh: use lakh numbering system

    Returns:
        str: words reprenting a number.
    """
    return Number(number, **kwargs).to_words()
