# -*- coding: utf-8 -*-

"""English language module."""

from .base import AbstractNumber


class Number(AbstractNumber):

    ZERO = 'zero'
    NEGATIVE = 'negative'
    ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    TEENS = [
        '', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen'
    ]
    TENS = [
        '', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety'
    ]
    HUNDREDS = [
        '', 'one hundred', 'two hundred', 'three hundred', 'four hundred',
        'five hundred', 'six hundred', 'seven hundred', 'eight hundred',
        'nine hundred'
    ]
    RANKS = [
        '', 'thousand', 'million', 'billion', 'trillion', 'quadrillion',
        'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion',
        'decillion', 'undecillion', 'duodecillion', 'tredecillion',
        'quattuordecillion', 'quindecillion', 'sexdecillion',
        'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion'
    ]
    CONJUNCTION = 'and'
    POINT = 'point'

    @classmethod
    def digits_to_words(cls, number, **kwargs):
        """Get words for each digit in a number

        Args:
            number (numeric): A whole number

        Returns:
            str: words for each digit in a number.

        """
        words = []

        digits = str(number)

        for i in digits:
            if float(i) == 0:
                words.append(cls.ZERO)
            else:
                words.append(cls.ONES[int(i)])

        return ' '.join(words)

    @classmethod
    def hundreds_to_words(cls, number):
        """Get a whole number within range less than one thousand in words.

        Args:
            number (numeric): a numeric value to be converted

        Returns
            str: numeric value in words.

        """
        words = []
        number = int(number) % 1000

        if number >= 100:
            hundred = number // 100
            hundredr = number % 100
            if hundredr:
                ten = hundredr // 10
                one = hundredr % 10
                words.append(cls.HUNDREDS[hundred])
                if ten:
                    words.append(cls.CONJUNCTION)
                    words.append(cls.TENS[ten])
                    if one:
                        words.append(cls.ONES[one])
                else:
                    words += [cls.CONJUNCTION, cls.ONES[one]]
            else:
                words.append(cls.HUNDREDS[hundred])

        elif 100 > number >= 10:
            if 20 > number > 10:
                teen = number - 10
                words.append(cls.TEENS[teen])
            else:
                ten = number // 10
                one = number % 10
                words.append(cls.TENS[ten])

                if one and not ten:
                    words.append(cls.CONJUNCTION)
                elif one:
                    words.append(cls.ONES[one])

        else:
            words.append(cls.ONES[number])

        if not words:
            return ''

        return ' '.join(words)

    @classmethod
    def short_scale_to_words(cls, number, use_lakh=False):
        """Get a value within a short scale range of a number in words.

        Args:
            number (numeric): An integer or a numeric string to be converted.

        Returns:
            str: numeric value within numbers short scale in words
        """
        words = []
        number = int(number)
        rank = cls.get_short_scale(number)
        hundred = number // 10**(3*rank)
        words = [cls.hundreds_to_words(hundred), cls.RANKS[rank]]

        return ' '.join(words)

    def to_words(self):
        """Get words representing the instance number.

        Returns:
            str: number in words.

        """
        words = []
        cls = self.__class__
        quotient = abs(float(self.quotient))

        if self.is_negative:
            words.append(cls.NEGATIVE)

        if quotient == 0:
            words.append(cls.ZERO)

        elif quotient < 1000:
            words.append(cls.hundreds_to_words(self.quotient))

        else:
            if quotient % 1000:
                if (quotient % 1000) < 100:
                    conjunction = cls.CONJUNCTION
                else:
                    conjunction = ','
            else:
                conjunction = None

            while quotient >= 1000:
                rank = self.get_short_scale(quotient)
                _next = quotient - (quotient // 10**(3*rank)) * (10**(3*rank))

                words.append(cls.short_scale_to_words(quotient))

                if _next >= 1000:
                    words.append(',')

                quotient = _next
            else:
                if conjunction:
                    words += [conjunction, cls.hundreds_to_words(quotient)]

        if self.is_decimal:
            words += [cls.POINT, cls.digits_to_words(self.fraction)]

        return ' '.join(words).replace(' , ', ', ')
