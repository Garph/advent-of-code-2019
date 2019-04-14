from dataclasses import dataclass
from collections import defaultdict
from event import create_event
from itertools import groupby

guards = defaultdict(list)

def pprint_night(date, guard_id, asleep):
   '''Pretty print a night on the job, e.g.,
       "10-31 # 677 ....##########################...######....................."
   '''
   print('{} #{:>4} {}'.format(
      date.strftime('%m-%d'), 
      guard_id, 
      ''.join(['#' if a else '.' for a in asleep])))


def by_night(e):
   '''Sort and group events by night'''
   return e.date.date()

with open('day_04/data.txt', 'r') as eventsfd:
   # Load events in order
   events = sorted(map(create_event, eventsfd.readlines()))

# Group events by night, and process each guard's sleeping habits
for date, events in groupby(sorted(events), key=by_night):
   asleep = [False] * 60   # Innocent until proven guilty for the first hour
   guard_id = None
   
   for event in events:
      if event.action == 'begins shift':
         guard_id = event.guard_id

      if event.action == 'falls asleep':
         asleep[event.minute:] = [True] * len(asleep[event.minute:])

      if event.action == 'wakes up':
         asleep[event.minute:] = [False] * len(asleep[event.minute:])
   
   # Add this night to their dictionary
   guards[guard_id].append(asleep)

# Which guard slept the most?
total_sleep = {}
for guard_id, nights in guards.items():
   total_sleep[guard_id] = sum(map(sum, nights))

sleepy_guy = max(total_sleep)

# Which minute of the night is the guard most likely to be asleep?
sleepy_minutes = list(map(sum, zip(*guards[sleepy_guy])))
most_slept_minute = sleepy_minutes.index(max(sleepy_minutes))

print('Guard {} slept the most during minute {}'
      .format(sleepy_guy, most_slept_minute))


# Of all guards, which guard is most frequently asleep on the same minute?
def most_frequently_asleep(guards):

   # maps a guard's ID to the number of nights they were asleep during each
   # minute of the night
   guard_habits = defaultdict(list)

   for guard_id, nights in guards.items():
      asleep_by_minute = [sum(minutes) for minutes in zip(*nights)]
      guard_habits[guard_id] = asleep_by_minute
   
   sleepiest_guard = None
   times_asleep = 0
   during_minute = None

   for guard_id, habits in guard_habits.items():
      for minute, sleep_count in enumerate(habits):
         if sleep_count > times_asleep:
            sleepiest_guard = guard_id
            times_asleep = sleep_count
            during_minute = minute

   print('Guard #{} slept during 00:{:0>2} {} times'.format(
      sleepiest_guard, during_minute, times_asleep))
      
most_frequently_asleep(guards)