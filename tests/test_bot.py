#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from labeler_site.bot import recognize_greeting

__author__ = "Quinn Zepeda"
__copyright__ = "Quinn Zepeda"
__license__ = "mit"


def test_recognize_greeting():
    assert recognize_greeting('Hi') is True
    assert recognize_greeting('Yo') is False
    assert recognize_greeting('') is False
    # with pytest.raises(AssertionError):
    #     fib(-10)
