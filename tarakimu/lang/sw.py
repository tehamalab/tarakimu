# -*- coding: utf-8 -*-

"""Swahili language module."""


class Number(object):
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

    def __init__(self, number, **kwargs):
        kwargs = kwargs or {}

        self.number = str(number)
        self.quotient = self.number.split('.')[0].replace('-', '')
        self.use_lakh = kwargs.get('use_lakh', False)

    @property
    def is_decimal(self):
        """bool: instance number is decimal."""
        return len(self.number.split('.')) > 1

    @property
    def is_negative(self):
        """bool: instance number is negative."""
        return self.number.startswith('-')

    @property
    def fraction(self):
        """str: fraction part of instance number."""
        f = self.number.split('.')

        if len(f) < 2:
            return ''

        return f[1]

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
                    words.append('na')
                    words.append(cls.TENS[ten])
                if one:
                    words.append('na')
                    words.append(cls.ONES[one])
            else:
                words.append(cls.HUNDREDS[hundred])

        if 100 > number >= 10:
            ten = number // 10
            one = number % 10
            words.append(cls.TENS[ten])

            if one:
                words.append('na')
                words.append(cls.ONES[one])

        elif number < 10:
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
                words += ['na', 'elfu', cls.hundreds_to_words(lakir)]
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
                words.append('sifuri')
            else:
                words.append(cls.ONES[int(i)])

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
                    conjunction = 'na'
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
            words += ['nukta', cls.digits_to_words(self.fraction)]

        return ' '.join(words).replace(' , ', ', ')
