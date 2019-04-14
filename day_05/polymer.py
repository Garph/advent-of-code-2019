# -----------------------------------------------------------------------------
# Packages
# -----------------------------------------------------------------------------

from copy import deepcopy
import sys

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def reactive(a, b):
   '''Two adjacent units within a polymer are reactive if they have the same 
   character but opposite polarity'''
   return (a != b) and (a.upper() == b.upper())


def react(polymer):
   """What is the length of the resulting fully-reacted polymer chain?"""

   size = len(polymer)
   index = 0

   while index < size - 1:
      # Post-Condition: The polyer is inert in range (0..index)

      if reactive(polymer[index], polymer[index + 1]):
         # Remove catalytic units from polymer chain
         del polymer[index: index + 2]
         size -= 2

         # Consider a chain reaction after the most recent removal
         if index != 0:
            index -= 1

      else:
         # Non-reactive, safe to advance
         index += 1
   
   return polymer


def remove_units(polymer, target):
   '''Removes a class of units from the polymer chain'''
   target_monomer = lambda unit: unit.upper() != target.upper()
   return list(filter(target_monomer, polymer))
   

# -----------------------------------------------------------------------------
# Script
# -----------------------------------------------------------------------------


def part_one(polymer):
   """What is the length of the resulting fully-reacted polymer chain?"""
   print(f"Resulting polymer's length: {len(react(deepcopy(polymer)))}")


def part_two(polymer):
   '''By removing all units of a given type, regardless of polarity, the
   polymer can collapse more completely. Which unit allows the shortest
   polymer?'''

   # Brute force it!
   result = {}
   for monomer in 'abcdefghijklmnopqrstuvwxyz':
      result[monomer] = len(react(remove_units(deepcopy(polymer), monomer)))

   smallest_reacted_polymer = min(result)

   print(f"The smallest reacted polymer is {result[smallest_reacted_polymer]}")

if __name__ == '__main__':
   # invoke with: `cat data.txt | xargs python polymer.py`

   polymer = list(sys.argv[1])
   part_one(polymer)
   part_two(polymer)