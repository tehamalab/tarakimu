# -*- coding: utf-8 -*-

"""Absarct language module."""


class AbstractNumber(object):

    def __init__(self, number, **kwargs):
        self.number = str(number)

    @property
    def quotient(self):
        """str: number quotient."""
        return self.number.split('.')[0].replace('-', '')

    @property
    def fraction(self):
        """str: fraction part of instance number."""
        f = self.number.split('.')

        if len(f) < 2:
            return ''

        return f[1]

    @property
    def is_decimal(self):
        """bool: instance number is decimal."""
        return len(self.number.split('.')) > 1

    @property
    def is_negative(self):
        """bool: instance number is negative."""
        return self.number.startswith('-')

    @staticmethod
    def get_short_scale(number):
        """Get short scale index of a number.

        Short scale system groups numbers based on powers of one thousand.

        Args:
            number (numeric): a numeric value to be ranked.

        Returns
            int: short scale index of a number, starting from 0.

        """
        rank = 0
        number = int(number)
        while number >= 1000:
            rank += 1
            number = number // 1000
        return rank
