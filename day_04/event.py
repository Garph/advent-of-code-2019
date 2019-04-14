from dataclasses import dataclass
from datetime import datetime, timedelta, date, time

@dataclass()
class event:
   '''Observations of guard's sleeping habits'''
   date: datetime
   minute: int
   guard_id: int
   action: str

   def __lt__(self, other):
      return self.date < other.date

def extract_guard_id(phrase):
   '''Extracts a guard ID out of a string'''
   # Find the first word with a '#' and tries to cast all but the first
   # character into an integer
   for word in phrase.split(' '):
      if '#' in word and str.isnumeric(word[1:]):
         return int(word[1:])
   return None

def schedule_adjustment(event):
   '''Guards may begin their shift before midnight, but they only sleep between
   00:00 and 01:00 the following day.
   
   `schedule_adjustment` relocates avents occuring between 23:00 and 00:00
   to 00:00 of the following day so sleeping habits can be attributed to the
   correct guard
   
   Warning: mutates event
   '''

   if event.date.hour == 23:
      # Relocate this event to beginning of following day
      next_day = event.date.date() + timedelta(days=1)
      midnight = time()
      event.minute = 0
      event.date = datetime.combine(next_day, midnight)

def create_event(record):
   '''Constructs an event from a record e.g.,

      '[1518-11-22 00:49] wakes up',
      '[1518-05-18 00:01] Guard #1171 begins shift',
      '[1518-11-20 00:28] falls asleep'

   Guards may begin their shift before midnight, but they only ever sleep
   between 00:00 and 01:00 the following day.
   '''

   # split "[1518-11-20 00:28] falls asleep" into 
   # ["[1518-11-20 00:28", "falls asleep"]
   date_str, action_str = record.strip().split('] ')

   # Parse date/time information
   date = datetime.strptime(date_str, '[%Y-%m-%d %H:%M')

   # relocates events occuring between 23:00 and 00:00 to midnight of the 
   # following day so sleeping habits can be attributed to the correct guard
   if date.hour == 23:
      next_day = date.date() + timedelta(days=1)
      midnight = time()
      date = datetime.combine(next_day, midnight)

   guard_id = extract_guard_id(action_str)
   action = action_str if guard_id == None else 'begins shift'

   return event(date, date.minute, guard_id, action)