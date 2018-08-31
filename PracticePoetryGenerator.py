# -*- coding: utf-8 -*-
"""
Author: Jennie Garcia
License: GNU General Public License v2
Date Created: Thursday, August 30, 2018

"""

import random

random.seed(0)

#list of nouns

nouns = ["mermaid", "sailor", "ocean", "waves", "water",
         "sand", "shore", "seashell"]

#list of verbs

verbs = ["swim", "run", "sink", "jump"]

#list of adjectives

adjectives = ["beautiful", "raucous", "fat", "ugly",
              "silly"]

noun = random.choice(nouns)

verb = random.choice(verbs)

adjective = random.choice(adjectives)

second_adjective = random.choice(adjectives)

#word poem
print "The" " " + adjective + " " + noun + " "

#for loop to iterate through verbs

i = 1

for verbs in verbs:
    whitespace = " " * i
    print whitespace + verb
    i = i + 1
    
#concatenation
print "The" " " + adjective + " " + noun + " " + verb
    
    
    

