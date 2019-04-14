import pytest
from day_04.event import *

from datetime import datetime

@pytest.mark.parametrize(
   ('phrase', 'guard_id'), [
   ('[1518-05-18 00:01] Guard #1171 begins shift', 1171),
   ('My name is Jonas', None),
   ('My name is agent #7', 7),
   ('#42', 42),
   ('#DoesNotComputer', None),
   ('', None),])
def test_extract_guard_id(phrase, guard_id):
   assert extract_guard_id(phrase) == guard_id

def test_create_event():
   
   event = create_event('[1518-11-22 00:49] wakes up')
   assert event.date == datetime(1518, 11, 22, 0, 49)
   assert event.minute == 49
   assert event.action == 'wakes up'
   assert event.guard_id == None

   event = create_event('[1518-05-18 00:01] Guard #1171 begins shift')
   assert event.date == datetime(1518, 5, 18, 0, 1)
   assert event.minute == 1
   assert event.action == 'begins shift'
   assert event.guard_id == 1171

   event = create_event('[1518-11-20 00:28] falls asleep')
   assert event.date == datetime(1518, 11, 20, 0, 28)
   assert event.minute == 28
   assert event.action == 'falls asleep'
   assert event.guard_id == None

def test_schedule_adjustment():

   # Don't modify events which occur after midnight
   event = create_event('[1518-05-18 00:49] Guard #1171 begins shift')
   schedule_adjustment(event)
   assert event.date == datetime(1518, 5, 18, 0, 49)
   assert event.minute == 49
   assert event.action == 'begins shift'
   assert event.guard_id == 1171

   # Modify events which occur before midnight to be at midnight
   # of the following day
   event = create_event('[1518-05-18 23:49] Guard #1171 begins shift')
   schedule_adjustment(event)
   assert event.date == datetime(1518, 5, 19, 0, 0)
   assert event.minute == 0
   assert event.action == 'begins shift'
   assert event.guard_id == 1171