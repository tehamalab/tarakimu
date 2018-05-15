#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tarakimu.num_to_words`."""

import pytest
from tarakimu import num_to_words


def test_num_to_words(numwords):
    """test num_to_words returns to right words for valid numbers"""
    for lang, samples in numwords.items():
        for n, w in samples.items():
            result = num_to_words(n, lang)
            assert result == w


def test_invalid_num_to_words(invalid_nums):
    """test num_to_words returns to right words for invalid numbers"""
    for n in invalid_nums:
        with pytest.raises(ValueError):
            num_to_words(n)
