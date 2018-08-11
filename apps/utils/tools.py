#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-7-7 下午10:49
# @Author  : Shark
# @File    : tools.py
# @Software: PyCharm


def format_time(value):
    value = str(value)
    time = value.replace('+00:00', '').replace('-', ' ')
    time = time.split(' ')
    return time[0] + '年' + time[1] + '月' + time[2] + '日' + ' ' + time[3]

