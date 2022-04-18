
#import numpy as np
#import pandas as pd

import pytest

#print('yes, pytest imported.')


def func(x):
    return x+1


def test_answer():
    assert func(3) == 5




