# coding=UTF-8
from Creature import Creature


class Person(Creature):
    """Person Class"""
    # class variable, shared by all instance
    basic_intelligence_level = 'LOW'

    def __init__(self, name):
        # 显示调用初始方法, 因为子类自定义了初始方法,反之,则不用
        Creature.__init__(self)
        self.name = name

    def say_hi(self):
        print('Hello!')

    @classmethod
    def intelli_level(cls):
        print(cls.basic_intelligence_level)
