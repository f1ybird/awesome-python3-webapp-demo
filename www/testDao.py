#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'kevin'

import orm
from models import User
import asyncio


# 测试dao方法
def test(loop, x):
    yield from orm.create_pool(loop, user='root', password='root', database='awesome')

    u = User(name='Test', email='test' + x + '@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


# test
loop = asyncio.get_event_loop()
for x in range(100):
    loop.run_until_complete(test(loop, str(x)))
