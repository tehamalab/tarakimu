#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tarakimu.num_to_words`."""

import pytest
from tarakimu import num_to_words


def test_num_to_words(numwords):
    """test num_to_words returns to right words for valid numbers"""
    for n, w in numwords.items():
        result = num_to_words(n)
        assert result == w


def test_invalid_num_to_words(invalid_nums):
    """test num_to_words returns to right words for invalid numbers"""
    for n in invalid_nums:
        with pytest.raises(ValueError):
            num_to_words(n)
