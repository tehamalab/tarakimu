# -*- coding: utf-8 -*-

import importlib


def get_lang(lang):
    """Get module for a give language.

    Args:
        lang (str): code representing the language.

        CUrrently the supported laguages are 'sw' and 'en' for Swahili and English.
    """
    return importlib.import_module('tarakimu.lang.{}'.format(lang))


def num_to_words(number, lang='sw', **kwargs):
    """Get number in words.

    Args:
        number (int): a numerical value to be converted.

        \*\*kwargs: a optional keyword arguments
            use_lakh (bool): use lakh numbering system in Swahili.

    Returns:
        str: words reprenting a number.
    """
    return get_lang(lang).Number(number, **kwargs).to_words()
