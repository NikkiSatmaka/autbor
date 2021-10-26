#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.disable()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

import random

coin = ['tails', 'heads']
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(f'guess is {guess}')

toss = random.randint(0, 1) # 0 is tails, 1 is heads
assert toss in [0, 1], f'Toss is {toss}. Toss has to be 0 or 1.'
toss = coin[toss]
logging.debug(f'guess is {guess}, toss is {toss}')

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug(f'guess is {guess}, toss is {toss}')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
