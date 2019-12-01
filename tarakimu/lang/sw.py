# -*- coding: utf-8 -*-

"""Swahili language module."""

from .base import AbstractNumber


class Number(AbstractNumber):

    ZERO = 'sifuri'
    NEGATIVE = 'hasi'
    ONES = ['', 'moja', 'mbili', 'tatu', 'nne', 'tano', 'sita', 'saba', 'nane', 'tisa']
    TENS = [
        '', 'kumi', 'ishirini', 'thelathini', 'arobaini', 'hamsini', 'sitini',
        'sabini', 'themanini', 'tisini'
    ]
    HUNDREDS = [
        '', 'mia moja', 'mia mbili', 'mia tatu', 'mia nne', 'mia tano',
        'mia sita', 'mia saba', 'mia nane', 'mia tisa'
    ]
    RANKS = [
        '', 'elfu', 'milioni', 'bilioni', 'trilioni', 'kuadrilioni',
        'kuintilioni', 'seksitilioni', 'septilioni', 'oktilioni', 'nonilioni',
        'desilioni', 'anidesilioni', 'dodesilioni', 'tradesilioni',
        'kuatuordesilion', 'kuindesilioni', 'seksidesilioni',
        'septendesilioni', 'oktodesilioni', 'novemdesilioni', 'vijintilioni'
    ]
    CONJUNCTION = 'na'
    POINT = 'nukta'

    def __init__(self, number, **kwargs):
        super(Number, self).__init__(number)

        kwargs = kwargs or {}
        self.use_lakh = kwargs.get('use_lakh', False)

    @classmethod
    def digits_to_words(cls, number):
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
                    words.append(cls.CONJUNCTION)
                    words.append(cls.ONES[one])
            else:
                words.append(cls.HUNDREDS[hundred])

        elif 100 > number >= 10:
            ten = number // 10
            one = number % 10
            words.append(cls.TENS[ten])

            if one:
                words.append(cls.CONJUNCTION)
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

            use_lakh (bool): Use Lakh (Laki) numbering system.
                Defaults to False.

        Returns:
            str: numeric value within numbers short scale in words.

        """
        number = int(number)
        words = []

        rank = cls.get_short_scale(number)

        hundred = number // 10**(3*rank)
        if rank == 1 and hundred >= 100 and use_lakh:
            laki = hundred // 100
            lakir = hundred % 100
            words += ['laki', cls.ONES[laki]]
            if lakir:
                words += [cls.CONJUNCTION, 'elfu', cls.hundreds_to_words(lakir)]
        else:
            words = [cls.RANKS[rank], cls.hundreds_to_words(hundred)]

        return ' '.join(words)

    @classmethod
    def short_scale_to_words_r(cls, number):
        """Get a value within the short scale range of a number in words
        with words representing scale added at the end.

        Args:
            number (numeric): An integer or a numeric string to be converted.

            use_lakh (bool): Use Lakh (Laki) numbering system.
                             Defaults to False.

        Returns:
            str: numeric value within numbers short scale in words.

        """
        number = int(number)
        words = []
        rank = cls.get_short_scale(number)
        words = [cls.hundreds_to_words(number // 10**(3*rank)), cls.RANKS[rank]]

        return ' '.join(words)

    def to_words(self):
        """Get words representing the instance number.

        Returns:
            str: number in words.

        """
        words = []
        cls = self.__class__
        quotient = abs(int(self.quotient))

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
                if (100000 <= quotient < 1000000) and not self.use_lakh:
                    words.append(cls.short_scale_to_words_r(quotient))
                else:
                    words.append(cls.short_scale_to_words(quotient, self.use_lakh))

                if _next >= 1000:
                    words.append(',')  # TODO: should allow either ',' or 'na'

                quotient = _next
            else:
                if conjunction:
                    words += [conjunction, cls.hundreds_to_words(quotient)]

        if self.is_decimal:
            words += [cls.POINT, cls.digits_to_words(self.fraction)]

        return ' '.join(words).replace(' , ', ', ')
