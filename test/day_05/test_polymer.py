# -----------------------------------------------------------------------------
# Packages
# -----------------------------------------------------------------------------

import pytest
from day_05.polymer import reactive, react, remove_units

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------

@pytest.mark.parametrize(
   'lhs,rhs,expected', [
   ('a', 'a', False),
   ('a', 'A', True),
   ('a', 'b', False)])
def test_reactive(lhs, rhs, expected):
   assert reactive(lhs, rhs) == expected

@pytest.mark.parametrize(
   'polymer, expected', [
   ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'),
   ('aaAA', ''),
   ('matThewW', 'mahe')
   ])
def test_react(polymer, expected):
   assert ''.join(react(list(polymer))) == expected

@pytest.mark.parametrize(
   'polymer,target,expected', [
      ('aaaaAAAAaaaa', 'a', ''),
      ('aaaaAAAAaaaa', 'A', ''),
      ('dabAcCaCBAcCcaDA', 'A', 'dbcCCBcCcD')])
def test_remove_units(polymer, target, expected):
   assert ''.join(remove_units(list(polymer), target)) == expected