# -*- coding: utf-8 -*-
"""
Author: Jennie Garcia
Description: Random Poetry Generator
License: GNU General Public License v2
Date Created: Tuesday, August 28, 2018
"""
import random

random.seed(0)


# list of nouns
nouns = ["dog", "cat", "mouse", "house", "woman", "shoe", "spider", "moon",
         "bird", "fly", "horse", "mouth"]

# list of verbs
verbs = ["swallow", "stomp", "smash", "scream", "jump", "throw",
         "hit", "run", "screech", "catch", "kick"]

# list of adjectives
adjectives = ["giant", "sneaky", "stealthy", "ugly", "fat", "gross",
              "raucous", "hungry", "arrogant"]

noun = random.choice(nouns)

verb = random.choice(verbs)

adjective = random.choice(adjectives)
second_adjective = random.choice(adjectives)

# word poem
print "The " + adjective + " " + noun + " " 

# for loop to iterate through verbs

i = 1
for verb in verbs:
    whitespace = " " * i
    print whitespace + verb
    i = i + 1

# concatenation


# string formatting

#i = 0
#for noun in nouns:
#    print nouns[i]
#    i = i + 1



