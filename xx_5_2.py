#! /usr/bin/python3.6

def in_fridge():
    try:
        count=fridge[wanted_food]
    except KeyError:
        count=0
    return count