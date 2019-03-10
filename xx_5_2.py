#! /usr/bin/python3.6

def in_fridge():
    '''这是一个函数判断冰箱中是否存在一个食物，aaa
    如果有返回数量，
    如果没有通过异常调用返回0'''
    try:
        count=fridge[wanted_food]
    except KeyError:
        count=0
    return count
