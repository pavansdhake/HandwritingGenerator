import Digit.constants as Constants
from PIL import Image
import random


def get_digit(digit):
    factor = random.randint(0, 4)
    switcher = {
        0: Image.open(Constants.zeros + str(factor) + '.jpeg'),
        1: Image.open(Constants.ones + str(factor) + '.jpeg'),
        2: Image.open(Constants.twos + str(factor) + '.jpeg'),
        3: Image.open(Constants.threes + str(factor) + '.jpeg'),
        4: Image.open(Constants.fours + str(factor) + '.jpeg'),
        5: Image.open(Constants.fives + str(factor) + '.jpeg'),
        6: Image.open(Constants.sixes + str(factor) + '.jpeg'),
        7: Image.open(Constants.sevens + str(factor) + '.jpeg'),
        8: Image.open(Constants.eights + str(factor) + '.jpeg'),
        9: Image.open(Constants.nines + str(factor) + '.jpeg'),
    }

    return switcher.get(digit, "nothing")


def get_number(number):
    res = Image.new('RGB', (155, 72), 'white')
    copy = number
    dig = []
    while copy > 0:
        temp = copy % 10
        copy = int(copy/10)
        dig.append(temp)
    dig.reverse()
    cursor = 0
    if len(dig) == 0:
        t = get_digit(0)
        res.paste(t, (cursor, random.randint(0, 8)))
    else:
        for digit in dig:
            t = get_digit(digit)
            res.paste(t, (cursor, 0))
            w, h = t.size
            cursor += w + 5
    return res
