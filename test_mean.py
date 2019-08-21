from mean import *

import math

def test_ints():
  nums = [4, 5, 28, 3]
  obs = mean(nums)
  exp = 10
  assert obs == exp

def test_negative():
  nums = [-3, 0, 0]
  obs = mean(nums)
  exp = -1
  assert obs == exp

def test_empty():
  nums = []
  obs = mean(nums)
  assert math.isnan(obs)
